from django.contrib import admin
from user import models as m
from django.contrib.auth.admin import UserAdmin as UserAdmin_
from django.utils.translation import gettext_lazy as _

# Register your models here.
# @admin.register(m.User)
# class UserAdmin(UserAdmin_):
#     fieldsets = (
#         (
#             None,
#             {
#                 "fields": (
#                     "username",
#                     "password",
#                     "phone_number",
#                     "role",
#                 )
#             },
#         ),
#         (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
#         (
#             _("Permissions"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 )
#             },
#         ),
#         (_("Important dates"), {"fields": ("last_login", "date_joined")}),
#     )

#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("username", "phone_number", "password1", "password2"),
#             },
#         ),
#     )


@admin.register(m.Admin)
class AdminUserAdmin(UserAdmin_):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                    "phone_number",
                )
            },
        ),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "phone_number", "password1", "password2"),
            },
        ),
    )


@admin.register(m.Student)
class StudentAdmin(UserAdmin_):
    fieldsets = (
        (None, {"fields": ("username", "password", "phone_number",
         "marks", "institute", "department", "semester", "batch_year","is_approved")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "phone_number",
                    "password1",
                    "password2",
                    "marks",
                    "institute",
                    "department",
                    "semester",
                    "batch_year",
                    "is_approved",
                ),
            },
        ),
    )


@admin.register(m.Volunteer)
class VolunteerAdmin(UserAdmin_):
    fieldsets = (
        (None, {"fields": ("username", "password", "phone_number",
                           "job_numbers", "department", "semester",
                           "volunteer_type", "reference","is_approved")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "phone_number",
                    "password1",
                    "password2",
                    "job_numbers",
                    "department",
                    "semester",
                    "volunteer_type",
                    "reference",
                    "is_approved",
                ),
            },
        ),
    )


@admin.register(m.DeptOfficer)
class DeptOfficerAdmin(UserAdmin_):
    fieldsets = (
        (None, {"fields": ("username", "password",
         "phone_number", "department", "address","is_approved")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "phone_number",
                    "password1",
                    "password2",
                    "department",
                    "address",
                    "is_approved"
                ),
            },
        ),
    )
