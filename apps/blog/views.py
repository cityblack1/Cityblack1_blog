from django.shortcuts import render
from django.db.models import Count


# Create your views here.

def recommend_articles(blog):
    from .models import BlogPage
    tag_ids = blog.tags.values_list('id', flat=True)
    similar_blog = BlogPage.objects.live().filter(tags__in=tag_ids).exclude(id=blog.id)
    similar_blog = similar_blog.annotate(same_tags=Count('tags')).order_by('-same_tags', '-date')[:2]
    return similar_blog