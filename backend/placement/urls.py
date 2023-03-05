from rest_framework.routers import DefaultRouter
from placement import views as v

router = DefaultRouter()
router.register(r"oncampus", v.OnCampusPlacedDetailViewSet, basename="oncampus")
router.register(r"offcampus", v.OffCampusPlacedDetailViewSet, basename="offcampus")
router.register(r"studentopening", v.StudentOpeningViewSet, basename="studentopening")
