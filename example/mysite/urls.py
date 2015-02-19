from django.conf.urls import patterns, include, url
from django.contrib import admin

from dproxy.views import DProxy


urlpatterns = patterns('',
    url(r'^python/(?P<url>.*)$', DProxy.as_view(base_url='http://python.org', rewrite=True)),

    url(r'^admin/', include(admin.site.urls)),
)
