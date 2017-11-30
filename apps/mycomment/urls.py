from .views import comment_view, contact_view

from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url
from mycomment import views


urlpatterns = [
    url(r'^contact/$', views.ContactList.as_view(), name='contact_me'),
    url(r'^contact/(?P<pk>[0-9]+)/$', views.ContactDetail.as_view()),
    url(r'^(?P<slug>.*?)/$', comment_view, name='blog_comment'),
]


urlpatterns = format_suffix_patterns(urlpatterns)