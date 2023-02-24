from django.db import models
from django.contrib.auth.models import AbstractUser
from typing import Optional, Iterable

# from user import managers
from user.roles import Role, VolunteerType
from django.contrib.auth.models import Permission
from functools import partial
from typing import List
from user.validators import number_validator
from utils.models import Approvable
# Create your models here.


class User(AbstractUser, Approvable):
    """
    `User` table contains ALL the users in the system.
    other classes like `Admin` `Student` `Volunteer` inherit from this class
    and are saved as a pointer to original `User` in table with other properties
    saved in their own table

    Hence, the _base_role is Undefined, Roles can be found at `users.roles.Role`
    """

    _base_role: Role = Role.UNDEFINED
    _predefined_permissions: List[str] = []

    role = models.PositiveSmallIntegerField(choices=Role.choices)
    phone_number = models.CharField(max_length=10, validators=[
                                    partial(number_validator, length=10)])

    def save(
        self,
        force_insert: bool = False,
        force_update: bool = False,
        using: Optional[str] = None,
        update_fields: Optional[Iterable[str]] = None,
    ) -> None:
        self.role = self._base_role
        saved_user = super().save(force_insert, force_update, using, update_fields)
        # assigning permissions AFTER the user is added in the database
        self.user_permissions.add(
            *[Permission.objects.get(codename=i) for i in self._predefined_permissions]
        )
        return saved_user


class Admin(User):
    _base_role = Role.ADMIN

    institute = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"

    def save(
        self,
        force_insert: bool = False,
        force_update: bool = False,
        using: Optional[str] = None,
        update_fields: Optional[Iterable[str]] = None,
    ) -> None:
        self.is_staff = True
        self.is_superuser = True
        self.is_approved = True
        return super().save(force_insert, force_update, using, update_fields)


class Student(User):
    _base_role = Role.STUDENT
    marks = models.IntegerField()
    institute = models.CharField(max_length=256)
    department = models.CharField(max_length=256)
    semester = models.CharField(max_length=1, blank=False)
    batch_year = models.DateField()  # 4 character field possible

    _predefined_permissions = ["view_student"]

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Volunteer(User):
    _base_role = Role.VOLUNTEER
    job_numbers = models.PositiveSmallIntegerField()
    department = models.CharField(max_length=256)
    semester = models.CharField(max_length=1, blank=False)
    volunteer_type = models.PositiveSmallIntegerField(
        choices=VolunteerType.choices)
    reference = models.TextField(max_length=2000, null=True)

    _predefined_permissions = ["view_volunteer"]

    class Meta:
        verbose_name = "Volunteer"
        verbose_name_plural = "Volunteers"


class DeptOfficer(User):
    _base_role = Role.DEPT_OFFICER
    department = models.CharField(max_length=256)
    address = models.TextField(max_length=2000)

    _predefined_permissions = ["view_deptofficer"]

    class Meta:
        verbose_name = "Department Officer"
        verbose_name_plural = "Department Officers"
