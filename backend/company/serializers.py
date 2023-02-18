from rest_framework import serializers
from company import models as m


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Company
        fields = '__all__'


class CurrentOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.CurrentOpening
        fields = '__all__'
