# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-07 04:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpage_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='feed_image',
        ),
    ]
