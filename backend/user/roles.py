from django.db.models import IntegerChoices


class Role(IntegerChoices):
    ADMIN = 1, "Admin"
    STUDENT = 2, "Student"
    VOLUNTEER = 3, "Volunteer"
    DEPT_OFFICER = 4, "Department Officer"
    UNDEFINED = 5, "Undefined"


class VolunteerType(IntegerChoices):
    LEADER = 1, "Leader"
    WORKER = 2, "Worker"
