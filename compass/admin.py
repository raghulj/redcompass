from django.contrib import admin
from compass.models import Compass


class CompassAdmin(admin.ModelAdmin):
    fields = ['latitude', 'longitude', 'last_ping']
    list_display = ('latitude', 'longitude', 'last_ping')



admin.site.register(Compass, CompassAdmin)