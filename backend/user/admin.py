from django.contrib import admin
from django.utils.functional import cached_property
from user import models as m
from django.contrib.auth.admin import UserAdmin as UserAdmin_
from django.utils.translation import gettext_lazy as _
from tnpapp.admin import append_primary_fields


# TODO : fix types
@admin.register(m.Admin)
class AdminUserAdmin(UserAdmin_):
    @cached_property
    def fieldsets(self):
        return super().fieldsets

    @cached_property
    def add_fieldsets(self):
        return super().fieldsets


@admin.register(m.Student)
class StudentAdmin(UserAdmin_):
    new_fields = (
        "phone_number",
        "enrollment_number",
        "marks",
        "institute",
        "department",
        "semester",
        "batch_year",
        "is_blocked",
    )

    readonly_fields = (
        "is_selected",
        "is_profile_complete",
    )

    @cached_property
    def list_filter(self):
        return (
            *super().list_filter,
            "is_selected",
            "is_profile_complete",
            "is_blocked",
        )

    @cached_property
    def fieldsets(self):
        return append_primary_fields(
            super().fieldsets, self.new_fields + self.readonly_fields
        )

    @cached_property
    def add_fieldsets(self):
        return append_primary_fields(super().add_fieldsets, self.new_fields)


@admin.register(m.Volunteer)
class VolunteerAdmin(UserAdmin_):
    new_fields = (
        "phone_number",
        # "job_numbers",
        "department",
        "semester",
        "volunteer_type",
        "reference",
    )

    @cached_property
    def fieldsets(self):
        return append_primary_fields(super().fieldsets, self.new_fields)

    @cached_property
    def add_fieldsets(self):
        return append_primary_fields(super().add_fieldsets, self.new_fields)


@admin.register(m.DeptOfficer)
class DeptOfficerAdmin(UserAdmin_):
    new_fields = (
        "phone_number",
        "department",
        "address",
    )

    @cached_property
    def fieldsets(self):
        return append_primary_fields(super().fieldsets, self.new_fields)

    @cached_property
    def add_fieldsets(self):
        return append_primary_fields(super().add_fieldsets, self.new_fields)
