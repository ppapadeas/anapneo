from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('anapneo.neo.views',
    (r'^$', TemplateView.as_view(template_name="index.html")),
)
