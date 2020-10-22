from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

class Incidences(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(srid=4326)
    objects = GeoManager()

    def __unicode__(self):
        return self.name    

    class Meta:
        verbose_name_plural = "Incidences"