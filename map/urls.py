from django.urls import path
from .views import geojson, static, place_detail

urlpatterns = [
    path('', static.index, name='index'),
    path('places.geojson', geojson.places_geojson, name='places_geojson'),
    path('api/places/<int:place_id>/', place_detail.place_detail, name='place_detail'),
]
