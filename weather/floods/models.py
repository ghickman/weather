from django.db import models
from django.contrib.gis.db.models import FloatField

class Flood(models.Model):
    # pk maps to register_#
    annual_dfo = models.IntegerField()
    country = models.TextField()
    began = models.datefield()
    ended = models.datefield()
    days = models.IntegerField()
    deaths = models.IntegerField()
    displaced = models.IntegerField(null=True, blank=True)
    damage_usd = models.IntegerField(null=True, blank=True)
    main_cause = models.TextField()
    severity = models.IntegerField()
    sq_km = models.DecimalField()
    flood_magnitude_index = models.DecimalField()
    centroid_x = FloatField()
    centroid_y = FloatField()


