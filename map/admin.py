from django.contrib import admin
from .models.place import Place
from .models.image import Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("title", "latitude", "longitude")
    inlines = [ImageInline]
