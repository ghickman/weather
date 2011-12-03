from django.conf.urls.defaults import patterns, include, url

from floods.views import LandingView

urlpatterns = patterns('',
  url(r'^$', LandingView.as_view(), name='FloodsHome'),
)
