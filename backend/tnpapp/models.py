from typing import Any, Tuple
from django.db import models
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404
from tnpapp.permissions import FineGrainedPermisions
from typing import List
from user.validators import number_validator
from django.contrib.auth.models import Permission
from functools import partial
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ApprovedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_approved=True)


class Approvable(models.Model):
    objects = models.Manager()
    is_approved = models.BooleanField(default=False)
    approved_objects = ApprovedManager()

    class Meta:
        abstract = True

class ApprovableModelSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ("is_approved",)


class CustomUser(AbstractUser, Approvable):
    _predefined_permissions: List[str] = []

    phone_number = models.CharField(
        max_length=10, validators=[partial(number_validator, length=10)]
    )

    def save(self, *args, **kwargs) -> None:
        saved_user = super().save(*args, **kwargs)
        # assigning permissions AFTER the user is added in the database
        self.user_permissions.add(
            *[Permission.objects.get(codename=i) for i in self._predefined_permissions]
        )
        return saved_user


class BaseCrudModelViewSet(ModelViewSet):
    # TODO : smaller serializer for all listing view and
    # detialed serializer for one entity view
    serializer_class: Any
    model_class: Any
    permission_classes = [FineGrainedPermisions]

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
