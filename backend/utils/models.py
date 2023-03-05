from typing import Any
from rest_framework.permissions import DjangoModelPermissions
from django.db import models
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404


class ApprovedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_approved=True)


class Approvable(models.Model):
    objects = models.Manager()
    is_approved = models.BooleanField(default=False)
    approved_objects = ApprovedManager()

    class Meta:
        abstract = True


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
