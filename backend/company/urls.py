from django.urls import path
from company import views as v


urlpatterns = [
    path('all/', v.get_companies),
    path('add/', v.add_company),
    path('delete/<int:id>', v.remove_company)
]
