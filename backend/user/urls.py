from django.urls import path 
from user import views as v

urlpatterns = [
    # path('add/admin/', v.insert_user_admin),
    path('add/student/', v.insert_user_student),
    path('add/deptofficer/', v.insert_user_deptofficer),
    path('add/volunteer/', v.insert_user_volunteer),
    path('login/', v.login_user),
    path('logout/', v.logout_user),
    path('me/', v.get_user),
    path('changepassword/', v.change_password),
    path('resume/<str:username>', v.generate_resume)
]
