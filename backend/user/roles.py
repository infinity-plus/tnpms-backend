from django.db.models import IntegerChoices


class VolunteerType(IntegerChoices):
    LEADER = 1, "Leader"
    WORKER = 2, "Worker"
