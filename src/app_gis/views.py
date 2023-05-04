from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Censustract, Censustract_New
from .serializers import (
    Geojson_Serializer,
    CensusCode_Serializer,
    Geojson_New_Serializer,
)
from django.db.models import Q
import geocoder


# @api_view(["GET"])
# def censuscode_to_geojson(request):
#     filterargs = request.query_params.dict()
#     censustract = Censustract.objects.filter(**filterargs)
#     serializer = Geojson_Serializer(censustract, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def censuscode_to_geojson(request):
    condition = Q()
    censuscodes = request.query_params.getlist("censuscode")
    queryset = Censustract.objects.all()
    for censuscode in censuscodes:
        condition |= Q(censuscode=censuscode)
    queryset = queryset.filter(condition)
    serializer = Geojson_Serializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def new_censuscode_to_geojson(request):
    condition = Q()
    censuscodes = request.query_params.getlist("censuscode")
    queryset = Censustract_New.objects.all()
    for censuscode in censuscodes:
        condition |= Q(censuscode=censuscode)
    queryset = queryset.filter(condition)
    serializer = Geojson_New_Serializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# TODO Change to Postgres to allow distinct on column
# censustract = Censustract.objects.filter(
#     censuscode__startswith=censuscode
# ).distinct("censuscode")[:5]
@api_view(["GET"])
def get_censuscode(request):
    censuscode = request.query_params.get("censuscode")
    censustract = Censustract.objects.filter(censuscode__contains=censuscode)[:15]
    serializer = CensusCode_Serializer(censustract, many=True)
    data = list(set([x["censuscode"] for x in serializer.data]))[:5]
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_lat_lon(request):
    location = geocoder.osm(request.query_params.get("address"))
    longitude = location.lng
    latitude = location.lat
    return Response([float(latitude), float(longitude)])
