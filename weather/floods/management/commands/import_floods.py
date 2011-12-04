from csv import reader
from datetime import datetime
from os.path import join

from django.conf import settings
from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand

from weather.floods.models import Flood

class Command(BaseCommand):
    def get_int(self, val):
        try:
            return int(val)
        except ValueError:
            return 0

    def handle(self, *args, **options):
        # grab the first file for now. Hack as hell but no time.
        with open(join(settings.DIRNAME, args[0]), 'r') as f:
            for row in reader(f, delimiter=','):
                print round(float(row[11]), 2)
                flood = Flood(
                    register_no = self.get_int(row[0]),
                    annual_dfo = self.get_int(row[1]),
                    country = row[2],
                    began = datetime.strptime(row[3], '%Y-%m-%d'),
                    ended = datetime.strptime(row[4], '%Y-%m-%d'),
                    days = row[5],
                    deaths = row[6],
                    displaced = self.get_int(row[7]),
                    damage_usd = self.get_int(row[8]),
                    main_cause = row[9],
                    severity = self.get_int(row[10]),
                    #sq_km = float(row[11]),
                    flood_magnitude_index = float(row[12]),
                    place = Point(float(row[13]), float(row[14]))
                )
                print flood
                flood.save()
                exit()

