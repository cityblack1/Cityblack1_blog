# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-12 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170911_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='read_times',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='阅读次数'),
        ),
    ]
