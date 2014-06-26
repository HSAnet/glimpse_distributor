from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

from distributor.packages.views import PackageVersionView, PackageUploadView


urlpatterns = patterns('',
    url(r'^version/$', PackageVersionView.as_view(), name='version'),
    url(r'^upload/$', csrf_exempt(PackageUploadView.as_view()), name='upload'),
)
