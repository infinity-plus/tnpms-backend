from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.request import Request
from company import models as m
from company import serializers as s
from rest_framework import permissions as rest_p
from company import permissions as model_p
from utils.models import derive_save_model_serializer

# Create your views here.


@swagger_auto_schema(method="get", responses={200: s.CompanySerializer(many=True)})
@api_view(["GET"])
def get_companies(req: Request):
    all_companies = m.Company.objects.all()
    data = s.CompanySerializer(all_companies, many=True)
    return Response(data.data, status=200)


@swagger_auto_schema(methods=["post"], request_body=s.CompanySerializer)
@api_view(["POST"])
@permission_classes([rest_p.IsAuthenticated, model_p.CanAddCompany])
@derive_save_model_serializer(s.CompanySerializer)
def add_company(req: Request):
    pass


@api_view(["POST"])
@permission_classes([rest_p.IsAuthenticated, model_p.CanDeleteCompany])
def remove_company(req: Request, id: int):
    m.Company.objects.get(id=id).delete()
    return Response(status=200)
