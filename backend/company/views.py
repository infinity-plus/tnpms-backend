from company import models as m
from company import serializers as s
from utils.models import BaseCrudModelViewSet
# Create your views here.


class CompanyCrudView(BaseCrudModelViewSet):
    serializer_class = s.CompanySerializer
    model_class = m.Company


class CurrentOpeningCrudView(BaseCrudModelViewSet):
    serializer_class = s.CurrentOpeningSerializer
    model_class = m.CurrentOpening
