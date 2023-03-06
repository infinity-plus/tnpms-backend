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
