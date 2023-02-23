from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions as p
from django.contrib.auth import login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from user import serializers as s
from user import models as m
from django.template import Context, Template
from xhtml2pdf import pisa  # type: ignore
from django.http import HttpResponse
from user.utils import link_callback
from typing import Callable, Any
from utils.models import derive_save_model_serializer

# Create your views here.


@swagger_auto_schema(methods=["post"], request_body=s.AdminSerializer)
@api_view(["POST"])
@derive_save_model_serializer(s.AdminSerializer)
def insert_user_admin(req: Request):
    pass


@swagger_auto_schema(methods=["post"], request_body=s.StudentSerializer)
@api_view(["POST"])
@derive_save_model_serializer(s.StudentSerializer)
def insert_user_student(req: Request):
    pass


@swagger_auto_schema(methods=["post"], request_body=s.VolunteerSerializer)
@api_view(["POST"])
@derive_save_model_serializer(s.VolunteerSerializer)
def insert_user_volunteer(req: Request):
    pass


@swagger_auto_schema(methods=["post"], request_body=s.DeptOfficerSerializer)
@api_view(["POST"])
@derive_save_model_serializer(s.DeptOfficerSerializer)
def insert_user_deptofficer(req: Request):
    pass


@swagger_auto_schema(methods=["post"], request_body=s.UserLoginSerializer)
@api_view(["POST"])
def login_user(req: Request):
    srlzr = s.UserLoginSerializer(data=req.data)
    if not srlzr.is_valid():
        return Response(srlzr.errors, status=400)

    user = m.User.objects.filter(username=srlzr.validated_data["username"]).first()
    if user is None:
        return Response("User Not Found in System", status=404)

    if not user.check_password(srlzr.validated_data["password"]):
        return Response("Wrong password", status=401)

    login(req, user)
    return Response(status=200)


@api_view(["GET"])
@permission_classes([p.IsAuthenticated])
def logout_user(req: Request):
    logout(req)
    return Response(status=200)


@swagger_auto_schema(methods=["post"], request_body=s.UserChangePasswordSerialzer)
@api_view(["POST"])
@permission_classes([p.IsAuthenticated])
def change_password(req: Request):
    serializer = s.UserChangePasswordSerialzer(data=req.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    if serializer.validated_data["password1"] != serializer.validated_data["password2"]:
        return Response("password do not match", status=400)

    req.user.set_password(serializer.validated_data["password1"])
    req.user.save()

    return Response(status=200)


@api_view(["GET"])
@permission_classes([p.IsAuthenticated])
def get_user(req: Request):
    return Response(req.user.get_username())


@api_view(["GET"])
def generate_resume(req: Request, username: str):
    user = m.Student.objects.filter(username=username).first()
    if user is None:
        return Response("User not Found", status=404)

    # dummy resume html template
    t = Template("<center><h1>{{ message }}</h1></center>.")

    # dummy context to render, dict is supposed to be
    # student details
    c = Context({"message": "Resume"})

    html = t.render(c)
    response = HttpResponse(content_type="application/pdf")
    response[
        "Content-Disposition"
    ] = f'attachment; filename="{user.username}_resume.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)

    # if errors while generateing pdf, return error
    if pisa_status.err:
        return Response(f"We had some errors <pre>{html}</pre>", status=500)

    return response
