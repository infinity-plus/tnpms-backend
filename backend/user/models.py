from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from user.roles import Department, VolunteerType
from tnpapp.models import CustomUser, UserRoles


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


class Student(CustomUser):
    marks = models.IntegerField()
    institute = models.CharField(max_length=256)
    # department = models.CharField(max_length=256)
    department = models.PositiveSmallIntegerField(choices=Department.choices)
    semester = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(8)]
    )
    batch_year = models.DateField()  # 4 character field possible
    is_profile_complete = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    is_selected = models.BooleanField(default=False)
    _predefined_permissions = ["view_student"]

    def save(self, *args, **kwargs) -> None:
        self.role = UserRoles.Student
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Volunteer(CustomUser):
    job_numbers = models.PositiveSmallIntegerField()
    department = models.CharField(max_length=256)
    semester = models.CharField(max_length=1, blank=False)
    volunteer_type = models.PositiveSmallIntegerField(choices=VolunteerType.choices)
    reference = models.TextField(max_length=2000, null=True)

    _predefined_permissions = ["view_volunteer"]

    def save(self, *args, **kwargs) -> None:
        self.role = UserRoles.Volunteer
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
