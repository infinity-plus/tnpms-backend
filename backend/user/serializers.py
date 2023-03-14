import datetime
from rest_framework import serializers
from user import models as m
from tnpapp.serializers import BaseUserModelSerializer
from typing import Any


# https://github.com/encode/django-rest-framework/issues/1926
class StudentSerializer(BaseUserModelSerializer):
    def calculate_semester(self, year: int) -> int:
        today = datetime.datetime.now()
        sem = (today.year - year) * 2
        if today.month > 5:
            sem += 1
        return sem

    def create(self, validated_data: Any):
        enr = validated_data["enrollment_number"]
        validated_data["batch_year"] = 2000 + int(enr[0:2])
        validated_data["institute"] = enr[2:5]
        validated_data["department"] = int(enr[7:9])
        validated_data["semester"] = self.calculate_semester(
            validated_data["batch_year"]
        )
        return super().create(validated_data)

    class Meta(BaseUserModelSerializer.Meta):
        model = m.Student
        extra_kwargs = {
            "is_selected": {"read_only": True},
            # TODO :  FIELD LEVEL PERMISSIONS, is_blocked should
            # only be editable by authorised people
            "is_blocked": {"read_only": True},
            "is_profile_complete": {"read_only": True},
            "institute": {"required": False},
            "department": {"required": False},
            "batch_year": {"required": False},
            "semester": {"required": False},
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
