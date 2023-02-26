from django.urls import path 
from company import views as v

urlpatterns = [
    # company URL patterns
    path("company/all/", v.get_companies),
    path("company/add/", v.add_company),
    path("company/delete/<int:id>", v.remove_company),
    # current openings
    path("opening/all/", v.get_current_openings),
    path("opening/add/", v.add_current_opening),
]
