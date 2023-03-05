from company import views as v
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"listings", v.CompanyCrudView, basename="listings")
router.register(r"currentopening", v.CurrentOpeningCrudView, basename="currentopening")
