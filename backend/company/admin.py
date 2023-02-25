from functools import cached_property
from django.contrib import admin
from company import models as m
from django.contrib.admin import ModelAdmin

# Register your models here.


@admin.register(m.Company)
class CompanyAdmin(ModelAdmin):
    list_display = (
        "name",
        "email_id",
        "hr_name",
        "industry_type",
        "company_type",
    )

    @cached_property
    def list_filter(self):
        return (*super().list_filter, "is_approved")


@admin.register(m.CurrentOpening)
class CurrentOpeningsAdmin(ModelAdmin):
    list_display = (
        "job_title",
        "opening_year",
        "nature_of_job",
        "vacancy_count",
        "min_package",
        "gender_preference",
    )

    @cached_property
    def list_filter(self):
        return (*super().list_filter, "is_approved")
