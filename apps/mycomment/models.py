from django.db import models
from django_comments_xtd.models import XtdComment


# Create your models here.


class MyComment(XtdComment):
    qq_num = models.IntegerField(verbose_name='QQ号', blank=True, null=True)


class Contact(models.Model):
    name = models.CharField(max_length=20, verbose_name='名字')
    email = models.EmailField(max_length=100, verbose_name='邮箱')
    subject = models.CharField(max_length=20, blank=True, verbose_name='专业')
    message = models.TextField(verbose_name='消息')
    date = models.DateTimeField(auto_now_add=True, verbose_name='发布日期', null=True, blank=True)

    class Meta:
        ordering = ['-date']