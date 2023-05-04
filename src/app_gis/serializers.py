from rest_framework import serializers
from .models import Censustract, Censustract_New

# class Full_Serializer(serializers.ModelSerializer):
#     """Return Censustract Data"""
#     class Meta:
#         model = Censustract
#         fields = "__all__"


class Geojson_Serializer(serializers.ModelSerializer):
    """Return Censustract Data"""

    class Meta:
        model = Censustract
        fields = ["geo_str", "censuscode", "blkgrpce", "state", "type"]


class CensusCode_Serializer(serializers.ModelSerializer):
    """Return Censustract Data"""

    class Meta:
        model = Censustract
        fields = ["censuscode"]


class Geojson_New_Serializer(serializers.ModelSerializer):
    """Return Censustract Data"""

    class Meta:
        model = Censustract_New
        fields = ["geojson", "censuscode", "blkgrpce", "state"]
