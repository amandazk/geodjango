from django.db import models

class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name    