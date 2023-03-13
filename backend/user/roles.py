from django.db.models import IntegerChoices


class Department(IntegerChoices):
    Computer = 7, "Computer Engineering"
    Automobile = 2, "Automobile Engineering"
    Civil = 6, "Civil Engineering"
    ElectricalElectronics = 8, "Electrical & Electronics Engineering"
    Electrical = 9, "Electrical Engineering"
    Infotech = 16, "Information Technology"
    Mechanical = 19, "Mechanical Engineering"


class VolunteerType(IntegerChoices):
    LEADER = 1, "Leader"
    WORKER = 2, "Worker"
