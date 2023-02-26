from django.db.models import QuerySet
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.request import Request
from company import models as m
from company import serializers as s
from rest_framework import permissions as rest_p
from utils.models import derive_save_model_serializer, show_approved_objects
from utils.permissions import DRFPermission

# Create your views here.


@swagger_auto_schema(method="get", responses={200: s.CompanySerializer(many=True)})
@api_view(["GET"])
@show_approved_objects(m.Company, s.CompanySerializer)
def get_companies(data: QuerySet):
    return data


@swagger_auto_schema(methods=["post"], request_body=s.CompanySerializer)
@api_view(["POST"])
@permission_classes([rest_p.IsAuthenticated, DRFPermission("company.add_company")])
@derive_save_model_serializer(s.CompanySerializer)
def add_company(req: Request):
    pass


@api_view(["POST"])
@permission_classes([rest_p.IsAuthenticated, DRFPermission("company.remove_company")])
def remove_company(req: Request, id: int):
    m.Company.objects.get(id=id).delete()
    return Response(status=200)
