from django.urls import path
from . import views

urlpatterns = [
    path('geojson', views.censuscode_to_geojson),
    path('new_geojson', views.new_censuscode_to_geojson),
    path('censuscode', views.get_censuscode),
    path('censuscode', views.get_censuscode),
    path('lat_lon', views.get_lat_lon),
]
