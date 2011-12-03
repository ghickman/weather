from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'weather.views.home', name='home'),
    # url(r'^floods/', include('weather.floods.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
