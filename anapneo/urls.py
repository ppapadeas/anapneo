from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('anapneo.neo.urls')),

    url(r'^browserid/', include('django_browserid.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        url(r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

    static_url = settings.STATIC_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        url(r'^%s/(?P<path>.*)$' % static_url, 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
    )
