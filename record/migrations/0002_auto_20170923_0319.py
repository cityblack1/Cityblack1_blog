# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-23 03:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20170917_1952'),
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagerecord',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='pagerecord',
            name='object_id',
        ),
        migrations.AddField(
            model_name='pagerecord',
            name='blog_page',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_page', to='blog.BlogPage'),
        ),
        migrations.AlterField(
            model_name='useraction',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='记录时间'),
        ),
        migrations.AlterField(
            model_name='useraction',
            name='title',
            field=models.CharField(max_length=50, verbose_name='行为/访问'),
        ),
    ]
