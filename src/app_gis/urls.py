from django.urls import path
from . import views

urlpatterns = [
    path('geojson', views.get_geojson),
    path('censuscode', views.get_censuscode),
]
