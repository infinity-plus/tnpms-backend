from django.db import models
from company.roles import CompanyType, Gender
from user.validators import number_validator
from functools import partial
from utils.models import Approvable

# Create your models here.


class Company(Approvable):
    name = models.CharField(max_length=256)
    email_id = models.EmailField()
    phone_number = models.CharField(max_length=10, validators=[
                                    partial(number_validator, length=10)])
    hr_name = models.CharField(max_length=256)
    address = models.TextField()
    company_relation = models.PositiveSmallIntegerField(
        choices=CompanyType.choices)
    # is mandatory in document but ONLY needed if company is a child
    parent_company_name = models.CharField(max_length=256, null=True)
    # possible to move to enum probably
    industry_type = models.CharField(max_length=256)
    current_employees = models.PositiveBigIntegerField()
    # possible to move to enum probably
    company_type = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class CurrentOpening(Approvable):
    job_title = models.CharField(max_length=256)
    opening_year = models.CharField(max_length=256)
    # supposed to be numeric 15? what exactly is nature, in a 15 digit number?
    nature_of_job = models.CharField(max_length=15, validators=[
                                     partial(number_validator, length=15)])
    short_description = models.CharField(max_length=256)
    long_description = models.TextField()
    min_qualification = models.PositiveIntegerField()
    specialization = models.CharField(max_length=256)
    special_skill_requirement = models.TextField()
    vacancy_count = models.PositiveIntegerField()
    # why number? possibly text about address
    vacancy_location = models.PositiveIntegerField()
    min_package = models.PositiveBigIntegerField()
    max_package = models.PositiveBigIntegerField()
    # supposed to be boolean, what about `ANY` type? nullable boolean?
    gender_preference = models.PositiveSmallIntegerField(
        choices=Gender.choices)
