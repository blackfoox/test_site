from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


class ImageInline(admin.TabularInline):
    """Возможность добавлять фото прямо в карточке места"""
    model = Image
    extra = 1
    fields = ('image', 'preview', 'position')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.image.url)
        return "Нет изображения"
    preview.short_description = "Превью"


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'latitude', 'longitude', 'photo_preview')
    inlines = [ImageInline]

    def photo_preview(self, obj):
        """Миниатюра первой фотографии в списке мест"""
        first_image = obj.images.first()
        if first_image:
            return format_html('<img src="{}" style="max-height: 60px;"/>', first_image.image.url)
        return "—"
    photo_preview.short_description = "Фото"
