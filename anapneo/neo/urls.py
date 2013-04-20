from django.conf.urls import patterns, include, url

urlpatterns = patterns('anapneo.neo.views',
    (r'^$', 'index'),
)
