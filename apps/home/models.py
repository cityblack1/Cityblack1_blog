from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.wagtailcore.models import Page

from blog.models import BlogPage, BlogIndexPage


class HomePage(Page):
    pass