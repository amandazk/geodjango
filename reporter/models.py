from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

class Incidences(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(srid=4326)
    objects = GeoManager()  
    geometry = models.PolygonField(srid=4326, null=True, geography=True)

    class Meta:
        verbose_name_plural = "Incidences"

    def __str__(self):
        return self.name

