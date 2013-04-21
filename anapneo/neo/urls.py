from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('anapneo.neo.views',
    url(r'^$', 'index', name='index.html'),
    url(r'^dashboard/$', 'dashboard', name='dashboard'),
    url(r'^register/$', 'register', name='register'),
    url(r'^neo/(?P<u_id>\d+)/$', 'neo_view', name='neo_view'),
    url(r'^neo/(?P<u_id>\d+)/edit/$', 'neo_edit', name='neo_edit'),
    url(r'^neo/create/$', 'neo_create', name='neo_create'),
    url(r'^u/(?P<slug>[a-z0-9-]+)/$', 'profile_view', name='profile_view'),
    url(r'^u/(?P<slug>[a-z0-9-]+)/edit/$', 'profile_edit', name='profile_edit'),
    url(r'dashboard/$', 'dashboard', name='dashboard'),
    url(r'about/$', 'about', name='about'),
    url(r'contact/$', 'contact', name='contact'),
)
