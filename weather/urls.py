from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
import os

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'weather.views.home', name='home'),
    # url(r'^floods/', include('weather.floods.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('weather.floods.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
         {'document_root': os.path.join(os.path.dirname(__file__), "media")}),
    )
