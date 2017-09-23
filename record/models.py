from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.

# 用户行为跟踪, 只跟踪Page页面的记录
class UserAction(models.Model):
    user = models.ForeignKey('users.User', null=True, blank=True, verbose_name='对应用户', related_name='action')

    url = models.CharField(max_length=150)
    ip_address = models.CharField(max_length=24, blank=True, verbose_name='Ip地址')

    # 一个记录可能对应着任何一个Page模型, 也可能什么都不对应
    content_type = models.ForeignKey(ContentType, null=True, blank=True, related_name='visit_record')
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey(ct_field='content_type', fk_field='object_id')

    title = models.CharField(max_length=50, verbose_name='行为/访问')

    # 记录用户的时间
    created = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')

    def get_user_all_actions(self):
        user = self.user
        return user.action.all()

    def get_page_all_actions(self):
        page = self.content_type
        return page.visit_record.all()

# 页面访问量记录
class PageRecord(models.Model):
    # 对应的model（Page）页面
    blog_page = models.OneToOneField('blog.BlogPage', related_name='blog_page', null=True, blank=True)

    last_visit = models.DateTimeField(auto_now=True)
    visit_times = models.IntegerField(default=0)


# 记录用户的搜索
class UserSearchRecord(models.Model):
    user = models.ForeignKey('users.User')
    search_field = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
