from django.views.generic import TemplateView

class LandingView(TemplateView):
  template_name = "floods/index.html"

class LocationView(TemplateView):
  template_name = "floods/location.html"

class FloodView(TemplateView):
  template_name = "floods/flood.html"
