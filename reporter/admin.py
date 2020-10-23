from django.contrib import admin
from .models import Incidences
from leaflet.admin import LeafletGeoAdmin

class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location', 'geometry')


admin.site.register(Incidences, IncidencesAdmin)
