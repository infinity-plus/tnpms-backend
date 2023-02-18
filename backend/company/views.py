from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.request import Request
from company import models as m
from company import serializers as s
from rest_framework import permissions as p
from user.models import User
from typing import cast

# Create your views here.


@swagger_auto_schema(method="get", responses={200: s.CompanySerializer(many=True)})
@api_view(["GET"])
def get_companies(req: Request):
    all_companies = m.Company.objects.all()
    data = s.CompanySerializer(all_companies, many=True)
    return Response(data.data, status=200)


@swagger_auto_schema(methods=["post"], request_body=s.CompanySerializer)
@api_view(["POST"])
def add_company(req: Request):
    if not cast(User, req.user).has_perm("company.add_company"):
        return Response("You dont have the permission to add a company", status=403)

    serializer = s.CompanySerializer(data=req.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    serializer.save()

    return Response(status=200)


@api_view(["POST"])
@permission_classes([p.IsAuthenticated])
def remove_company(req: Request, id: int):
    if not cast(User, req.user).has_perm("company.delete_company"):
        return Response("You dont have the permission to delete a company!", status=403)

    m.Company.objects.get(id=id).delete()
    return Response(status=200)
