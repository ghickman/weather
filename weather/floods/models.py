from django.contrib.gis.db import models

class Flood(models.Model):
    register_no = models.IntegerField()
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
    place = models.PointField()

    def __unicode__(self):
        return '%s to %s at %s' % (self.began, self.ended, self.place)


