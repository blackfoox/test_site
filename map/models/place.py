from django.db import models


class Place(models.Model):
    """Место, отображаемое на карте."""
    title = models.CharField("Название", max_length=200)
    description_short = models.TextField("Краткое описание", blank=True)
    description_long = models.TextField("Полное описание", blank=True)
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return self.title