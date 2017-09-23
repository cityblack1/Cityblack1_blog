from django.core.management import call_command

import os
import django

__author__ = 'cityblack1'

__doc__ ="""
模拟命令行启动, 用于IDE调试
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_blog.settings.dev')
django.setup()
call_command('runserver')
