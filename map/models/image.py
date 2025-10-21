from django.db import models
from .place import Place

class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Место"
    )
    image = models.ImageField("Фотография", upload_to="places")
    position = models.PositiveIntegerField("Порядковый номер", default=0)

    class Meta:
        ordering = ["position"]
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return f"{self.position} – {self.place.title}"

