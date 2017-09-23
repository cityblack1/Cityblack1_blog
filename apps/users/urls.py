from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib.auth.views import logout

from users.views import login as user_login
from users.views import register


urlpatterns = [
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', logout, {'redirect_field_name': 'next', 'template_name': 'home/home_page.html'}, name='logout'),
    url(r'^register/$', register, name='register'),
]
