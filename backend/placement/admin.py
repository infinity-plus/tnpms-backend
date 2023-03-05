from django.contrib import admin
from placement import models as m

# Register your models here.


@admin.register(m.StudentOpening)
class StudentOpeningManager(admin.ModelAdmin):
    pass


@admin.register(m.OnCampusPlacedDetail)
class OnCampusPlacedDetailManager(admin.ModelAdmin):
    pass


@admin.register(m.OffCampusPlacedDetail)
class OffCampusPlacedDetailManager(admin.ModelAdmin):
    pass
