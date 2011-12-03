from django.db import models
from django.contrib.gis.db.models import FloatField

class Flood(models.Model):
    register_id = models.IntegerField()
    annual_dfo = models.IntegerField()
    country = models.TextField()
    began = models.DateField()
    ended = models.DateField()
    days = models.IntegerField()
    deaths = models.IntegerField()
    displaced = models.IntegerField(null=True, blank=True)
    damage_usd = models.IntegerField(null=True, blank=True)
    main_cause = models.TextField()
    severity = models.IntegerField()
    sq_km = models.DecimalField(decimal_places=9, max_digits=10)
    flood_magnitude_index = models.DecimalField(decimal_places=9, max_digits=10)
    centroid_x = FloatField()
    centroid_y = FloatField()


