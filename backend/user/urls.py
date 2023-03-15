from django.urls import include, path
from rest_framework.routers import DefaultRouter
from user import views as v

router = DefaultRouter()
router.register(r"student", v.StudentCrudView, basename="student")
router.register(r"volunteer", v.VolunteerCrudView, basename="volunteer")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", v.login_user),
    path("logout/", v.logout_user),
    path("me/", v.get_user),
    path(
        "register/student/",
        v.StudentRegistrationView.as_view(),
        name="student-registration-view",
    ),
    path("resume/<str:username>", v.generate_resume),
]
