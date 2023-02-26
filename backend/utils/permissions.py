from typing import Type
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView


def DRFPermission(perm_string: str) -> Type[BasePermission]:
    class _(BasePermission):
        def has_permission(self, request: Request, view: APIView) -> bool:
            return request.user.has_perm(perm_string)

    return _
