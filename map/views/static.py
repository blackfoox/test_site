from django.shortcuts import render
from map.models.place import Place

def index(request):
    places = Place.objects.all()

    context = {
        'places': places
    }

    return render(request, 'map/index.html', context)