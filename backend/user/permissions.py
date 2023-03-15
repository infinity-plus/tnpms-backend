from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request: Request, view: APIView , obj):
        return request.user.id == obj.id

class Registerable(permissions.BasePermission):
    """
    Allow objects like student/volunteer to register themnselves
    """

    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == "POST":
            return True

        return False
