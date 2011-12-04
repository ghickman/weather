from django.conf.urls.defaults import patterns, include, url

from floods.views import LandingView
from floods.views import LocationView
from floods.views import FloodView

urlpatterns = patterns('',
  url(r'^$', LandingView.as_view(), name='FloodsHome'),
  url(r'^location/$', LocationView.as_view(), name='FloodsLocationInfo'),
  url(r'^flood/(?P<pk>\d+)$', FloodView.as_view(), name='FloodsFloodDetail'),
)
