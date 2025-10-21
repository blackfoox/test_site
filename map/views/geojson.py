from django.http import JsonResponse
from map.models.place import Place

def places_geojson(request):
    places = Place.objects.all().prefetch_related('images')
    features = []

    for place in places:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude],
            },
            "properties": {
                "title": place.title,
                "id": place.id,
            },
        })

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return JsonResponse(geojson)
