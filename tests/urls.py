"""
A URLs module to satisfy the test project.
"""

from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView


urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url="https://www.djangoproject.com")),
)


urlpatterns += staticfiles_urlpatterns()
