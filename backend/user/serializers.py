from rest_framework import serializers
from typing import Any
from functools import wraps
from user import models as m
from utils.serializer import DeriveBaseUserSerializer


@DeriveBaseUserSerializer(m.Admin)
class AdminSerializer(serializers.ModelSerializer):
    pass


@DeriveBaseUserSerializer(m.Student)
class StudentSerializer(serializers.ModelSerializer):
    pass


@DeriveBaseUserSerializer(m.DeptOfficer)
class DeptOfficerSerializer(serializers.ModelSerializer):
    pass


@DeriveBaseUserSerializer(m.Volunteer)
class VolunteerSerializer(serializers.ModelSerializer):
    pass


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=False)
    password = serializers.CharField(allow_blank=False)


class UserChangePasswordSerialzer(serializers.Serializer):
    password1 = serializers.CharField(allow_blank=False)
    password2 = serializers.CharField(allow_blank=False)
