# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-14 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170913_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='user/%Y/%m', verbose_name='头像'),
        ),
    ]
