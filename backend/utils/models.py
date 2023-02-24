from typing import Callable, Any
from rest_framework.request import Request
from rest_framework.response import Response
from django.db import models


def derive_save_model_serializer(serializer_class: Any):
    """
    This decorator is destructive, it re-assgines the function body itself
    and whatever which was previously defined in the ORIGINAL function
    will not remain and will not be executed.
    """

    def _decorator(func: Callable):
        def wrapper(req: Request):
            serializer = serializer_class(data=req.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=400)
            serializer.save()

            return Response(status=200)

        return wrapper

    return _decorator


class ApprovedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_approved=True)


class Approvable(models.Model):
    objects = models.Manager()
    is_approved = models.BooleanField(default=False)
    approved_objects = ApprovedManager()

    class Meta:
        abstract = True
