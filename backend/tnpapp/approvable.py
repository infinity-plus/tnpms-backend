from django.db import models


class ApprovedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_approved=True)


class Approvable(models.Model):
    objects = models.Manager()
    is_approved = models.BooleanField(default=False)
    approved_objects = ApprovedManager()

    class Meta:
        abstract = True


class ApprovableMetaMixin:
    """
    Usage:
    from rest_framework import serializers

    class A(serializers.ModelSerializer):
        class Meta(ApprovableMetaMixin):
            # attributes
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if not hasattr(self, "read_only_fields"):
            self.read_only_fields = ()
        self.read_only_fields += (("is_approved"),)


class ApprovableModelFilterMixin:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if not hasattr(self, "list_filter"):
            self.list_filter = ()
        self.list_filter += ("is_approved",)


class ApprovableAdminMixin(ApprovableModelFilterMixin):
    """
    ADD MIXIN BEFORE EXTENDING WITH THE BASE CLASS
    Usage:
    class A(Mixin, B, C):
        pass
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # assuming self.fieldsets and self.add_fieldsets are already set
        self.fieldsets[0][1]["fields"] += ("is_approved",)  # type: ignore
        self.add_fieldsets[0][1]["fields"] += ("is_approved",)  # type: ignore
