from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import action

urlpatterns = [
    url(r'^action/$', action, name='action'),
]