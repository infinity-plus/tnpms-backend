from django.db.models import IntegerChoices


class CompanyType(IntegerChoices):
    PARENT = 1, "Parent"
    CHILD = 2, "Child"


class Gender(IntegerChoices):
    MALE = 1, "Male"
    FEMALE = 2, "Female"
    ANY = 3, "Any"
