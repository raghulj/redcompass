from django.db import models

class Compass(models.Model):
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    last_ping = models.DateTimeField('date located')
