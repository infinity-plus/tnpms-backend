from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView


class CanDeleteCompany(BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        return request.user.has_perm("company.delete_company")


class CanAddCompany(BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        return request.user.has_perm("company.add_company")
