from functools import wraps
from typing import Any


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
