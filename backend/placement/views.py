from django.shortcuts import render
from placement import models as m, serializers as s
from tnpapp.models import BaseCrudModelViewSet

# Create your views here.


class OnCampusPlacedDetailViewSet(BaseCrudModelViewSet):
    serializer_class = s.OnCampusPlacedDetailSerializer
    model_class = m.OnCampusPlacedDetail


class OffCampusPlacedDetailViewSet(BaseCrudModelViewSet):
    serializer_class = s.OffCampusPlacedDetailSerializer
    model_class = m.OffCampusPlacedDetail


class StudentOpeningViewSet(BaseCrudModelViewSet):
    serializer_class = s.StudentOpeningSerializer
    model_class = m.StudentOpening
