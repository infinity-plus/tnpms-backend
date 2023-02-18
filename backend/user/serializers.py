from rest_framework import serializers
from typing import Any
from functools import wraps
from user import models as m


def DeriveBaseUserSerializer(klass: Any):
    def decorator(cls: Any):
        @wraps(klass, updated=())
        class Temp(cls):
            class Meta:
                model = klass
                exclude = (
                    "is_staff",
                    "is_superuser",
                    "is_active",
                    "role",
                    "user_permissions",
                    "groups",
                    "last_login",
                    "date_joined",
                )
                extra_kwargs = {"password": {"write_only": True}}

            def save(self, **kwargs):
                return self.Meta.model.objects.create_user(**self.validated_data)

        return Temp

    return decorator


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
