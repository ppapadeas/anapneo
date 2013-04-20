from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('anapneo.neo.views',
    url(r'^$', 'index'),
    url(r'dashboard/$', 'dashboard'),
    url(r'about/$', 'about'),
    url(r'contact/$', 'contact'),
)
