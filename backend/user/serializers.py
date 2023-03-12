from rest_framework import serializers
from user import models as m
from tnpapp.serializers import BaseUserModelSerializer


# https://github.com/encode/django-rest-framework/issues/1926
class StudentSerializer(BaseUserModelSerializer):
    class Meta(BaseUserModelSerializer.Meta):
        model = m.Student
        extra_kwargs = {
            "is_selected": {"read_only": True},
            "is_profile_complete": {"read_only": True},
        }


class DeptOfficerSerializer(BaseUserModelSerializer):
    class Meta(BaseUserModelSerializer.Meta):
        model = m.DeptOfficer


class VolunteerSerializer(BaseUserModelSerializer):
    class Meta(BaseUserModelSerializer.Meta):
        model = m.Volunteer


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=False)
    password = serializers.CharField(allow_blank=False)
