from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

from distributor.packages.views import PackageUploadView


urlpatterns = patterns('',
    url(r'^upload/$', csrf_exempt(PackageUploadView.as_view()), name='upload'),
)
