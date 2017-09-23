from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from api.views import check_username, check_email


urlpatterns = [
    url(r'^ck_un/$', check_username, name='check_username'),
    url(r'^ck_email/$', check_email, name='check_email'),
]
