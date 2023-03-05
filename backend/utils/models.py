from typing import Callable, Any, Type
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.request import Request
from rest_framework.response import Response
from django.db import models
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404

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


def model_field_exist(model: Any, field: str) -> bool:
    return field in [i.name for i in model._meta.get_fields(include_hidden=True)]

def show_approved_objects(model_class:Type[Approvable], serializer_class: Any):
    """
    This decorator is destructive, it re-assgines the function body itself
    and whatever which was previously defined in the ORIGINAL function
    will not remain and will not be executed.
    """
    def _decorator(func: Callable):
        def wrapper(req: Request):
            _sort = req.GET.dict().get('sort')
            data = model_class.approved_objects.all()
            if _sort is not None and model_field_exist(model_class, _sort.replace('-','')):
                data = data.order_by(_sort)
            
            data = func(data)

            serializer = serializer_class(data, many=True)
            return Response(serializer.data, status=200)

        return wrapper

    return _decorator

class BaseCrudModelViewSet(ModelViewSet):
    # TODO : smaller serializer for all listing view and
    # detialed serializer for one entity view
    serializer_class: Any
    model_class: Any
    permission_classes = [DjangoModelPermissions]
    
    # for filtering
    # https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend

    def get_object(self):
        return get_object_or_404(self.model_class, id=self.kwargs["pk"])

    def get_queryset(self):
        """
        add is_approved here or is_active filter here
        filtering code below for reference, DO NOT USE IN PRODUCTION
        return self.model_class.objects.filter(**self.request.GET.dict())
        """
        return self.model_class.objects.all()
