from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin

urlpatterns = patterns('',
    url(r'^packages/', include('distributor.packages.urls', namespace='packages')),

    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
