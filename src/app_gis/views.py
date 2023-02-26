from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Censustract
from .serializers import Geojson_Serializer, CensusCode_Serializer


@api_view(["GET"])
def get_geojson(request):
    filterargs = request.query_params.dict()
    censustract = Censustract.objects.filter(**filterargs)
    serializer = Geojson_Serializer(censustract, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_censuscode(request):
    censuscode = request.query_params.get("censuscode")
    censustract = Censustract.objects.filter(censuscode__startswith=censuscode)[:5]
    serializer = CensusCode_Serializer(censustract, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
