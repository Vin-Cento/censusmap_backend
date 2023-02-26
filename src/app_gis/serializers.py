from rest_framework import serializers
from .models import Censustract


class Geojson_Serializer(serializers.ModelSerializer):
    """Return Censustract Data"""
    class Meta:
        model = Censustract
        fields = "__all__"

class CensusCode_Serializer(serializers.ModelSerializer):
    """Return Censustract Data"""
    class Meta:
        model = Censustract
        fields = ['censuscode']
