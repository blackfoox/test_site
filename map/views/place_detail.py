from django.shortcuts import get_object_or_404
from map.models.place import Place
from django.http import JsonResponse

def place_detail(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), id=place_id)

    data = {
        "title": place.title,
        "imgs": [img.image.url for img in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.latitude,
            "lng": place.longitude,
        },
    }

    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
