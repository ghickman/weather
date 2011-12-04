from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.sites.models import Site

from weather.floods.models import Flood

admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(User)
admin.site.register(Flood)
