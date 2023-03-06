from rest_framework import serializers
from user import models as m
from tnpapp.serializers import BaseUserModelSerializer


class StudentSerializer(BaseUserModelSerializer):
    class Meta(BaseUserModelSerializer.Meta):
        model = m.Student


class DeptOfficerSerializer(BaseUserModelSerializer):
    class Meta(BaseUserModelSerializer.Meta):
        model = m.DeptOfficer


class VolunteerSerializer(BaseUserModelSerializer):
    class Meta(BaseUserModelSerializer.Meta):
        model = m.Volunteer


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=False)
    password = serializers.CharField(allow_blank=False)
