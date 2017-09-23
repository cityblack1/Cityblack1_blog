from functools import reduce

from django.db.models import Q
from blog.models import BlogPage, BlogIndexPage

from taggit.models import Tag

all_blog = None
blog_index = None
date_category = None
tags_list = None

def reset_data():
    global all_blog, blog_index, date_category, tags_list
    all_blog = BlogPage.objects.live().order_by('-first_published_at')
    # 缓存所有blog
    _ = [blog for blog in all_blog]
    blog_index = BlogIndexPage.objects.live().order_by('-first_published_at')
    # all_tags = [blog.tags.all().results for blog in _ if blog.tags.all()]
    # try:
    #     tags_list = list(set(tag.name for tag in reduce(lambda x, y: x + y, all_tags)))
    # except:
    #     tags_list = []
    tags_list = [tag.name for tag in Tag.objects.all()]
    months = all_blog.dates('date', 'month', order='DESC')
    date_category = [all_blog.filter(Q(date__year=month.year) & Q(date__month=month.month)) for month in months]

reset_data()


def blogs(request):
    return {
        'blogs': all_blog,
        'blog_index': blog_index,
        'date_categories': date_category,
        'tags_list': tags_list,
    }
