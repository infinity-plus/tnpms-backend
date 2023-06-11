from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from user.roles import Department, VolunteerType
from tnpapp.models import CustomUser, UserRoles
import datetime
from user.validators import number_validator
from functools import partial


# ALL USER MODELS
class AdminUserManager(UserManager):
    def get_queryset(self) -> models.QuerySet[AbstractUser]:
        return super().get_queryset().filter(is_superuser=True)


class Admin(CustomUser):
    objects = AdminUserManager()

    class Meta:
        proxy = True
        verbose_name = "Admin"
        verbose_name_plural = "Admins"

    def save(self, *args, **kwargs) -> None:
        """
        `self.pk` // primary key doesnt exist when model
        is not yet saved in database
        """
        if not self.pk:
            self.is_staff = True
            self.is_superuser = True
            # is_approved will be used if Custom User is extending
            # Approvable Mixin, else its just phantom data
            self.is_approved = True
        self.role = UserRoles.Admin
        return super().save(*args, **kwargs)


# TODO :  add d2d
def calculate_semester(year: int) -> int:
    today = datetime.datetime.now()
    sem = (today.year - year) * 2
    if today.month > 5:
        sem += 1
    return sem


class Student(CustomUser):
    enrollment_number = models.CharField(
        max_length=12, validators=[partial(number_validator, length=12)], unique=True
    )
    marks = models.IntegerField(blank=True, null=True)
    institute = models.CharField(
        max_length=3, validators=[partial(number_validator, length=3)]
    )
    department = models.PositiveSmallIntegerField(choices=Department.choices)
    semester = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)]
    )
    batch_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(2012),
            MaxValueValidator(datetime.datetime.now().year),
        ]
    )
    is_profile_complete = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    is_selected = models.BooleanField(default=False)
    _predefined_permissions = ["view_student"]

    def save(self, *args, **kwargs) -> None:
        self.role = UserRoles.Student
        if not self.pk:
            enr = self.enrollment_number
            if not self.department:
                self.department = int(enr[7:9])
            if not self.batch_year:
                self.batch_year = 2000 + int(enr[:2])
            if not self.institute:
                self.institute = enr[2:5]
            if not self.semester:
                self.semester = calculate_semester(self.batch_year)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Volunteer(CustomUser):
    # why was this needed in the first place?
    # job_numbers = models.PositiveSmallIntegerField()
    enrollment_number = models.CharField(
        max_length=12, validators=[partial(number_validator, length=12)]
    )
    department = models.PositiveSmallIntegerField(choices=Department.choices)
    semester = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)]
    )
    volunteer_type = models.PositiveSmallIntegerField(
        choices=VolunteerType.choices, default=VolunteerType.WORKER
    )
    reference = models.TextField(max_length=2000, null=True)

    _predefined_permissions = ["view_volunteer"]

    def save(self, *args, **kwargs) -> None:
        self.role = UserRoles.Volunteer
        if not self.pk:
            enr = self.enrollment_number
            if not self.department:
                self.department = int(enr[7:9])
            if not self.semester:
                self.semester = calculate_semester(2000 + int(enr[:2]))

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Volunteer"
        verbose_name_plural = "Volunteers"


class DeptOfficer(CustomUser):
    department = models.CharField(max_length=256)
    address = models.TextField(max_length=2000)

    _predefined_permissions = ["view_deptofficer"]

    def save(self, *args, **kwargs) -> None:
        self.role = UserRoles.DepartmentOfficer
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Department Officer"
        verbose_name_plural = "Department Officers"
