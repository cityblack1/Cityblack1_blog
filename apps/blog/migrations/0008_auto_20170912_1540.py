# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-12 15:40
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170912_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', label='测试')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('markdown', wagtail.wagtailcore.blocks.TextBlock(icon='code')))),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', label='测试')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('markdown', wagtail.wagtailcore.blocks.TextBlock(icon='code')))),
        ),
    ]
