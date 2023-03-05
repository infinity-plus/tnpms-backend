from rest_framework import serializers
from placement import models as m


class OnCampusPlacedDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.OnCampusPlacedDetail
        fields = "__all__"


class OffCampusPlacedDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.OffCampusPlacedDetail
        fields = "__all__"


class StudentOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.StudentOpening
        fields = "__all__"
