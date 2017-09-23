from __future__ import absolute_import, unicode_literals

from django.db.models import Q
from django.shortcuts import render

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.models import Query

from blog.models import BlogPage, BlogIndexPage


def search(request):
    tag = request.GET.get('t', None)
    if tag:
        search_results = BlogPage.objects.live().filter(tags__name=tag)
        return render(request, 'search/search_result.html', {
            'search_query': None,
            'blogs': search_results,
            'tag': tag,
            'category': None,
        })

    category = request.GET.get('c', None)
    if category:
        cate = BlogIndexPage.objects.live().get(slug=category)
        title = cate.title
        search_results = cate.get_descendants()
        search_results = [x.specific for x in search_results]
        return render(request, 'search/search_result.html', {
            'search_query': None,
            'blogs': search_results,
            'category': title,
            'tag': None,
        })

    date = request.GET.get('date', None)
    if date:
        year, month = date.split('m')
        search_query = year + '年' + month + '月'
        search_results = BlogPage.objects.live().filter(Q(date__year=year) & Q(date__month=month))
        return render(request, 'search/search_result.html', {
            'search_query': search_query,
            'blogs': search_results,
            'category': None,
            'tag': None,
        })

    search_query = request.GET.get('query', None)
    # Search
    if search_query:
        search_results = BlogPage.objects.live().search(search_query, operator='or')
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    return render(request, 'search/search_result.html', {
        'search_query': search_query,
        'blogs': search_results,
        'category': None,
        'tag': None,
    })








# def search(request):
#     search_query = request.GET.get('query', None)
#     page = request.GET.get('page', 1)
#
#     # Search
#     if search_query:
#         search_results = Page.objects.live().search(search_query)
#         query = Query.get(search_query)
#
#         # Record hit
#         query.add_hit()
#     else:
#         search_results = Page.objects.none()
#
#     # Pagination
#     paginator = Paginator(search_results, 10)
#     try:
#         search_results = paginator.page(page)
#     except PageNotAnInteger:
#         search_results = paginator.page(1)
#     except EmptyPage:
#         search_results = paginator.page(paginator.num_pages)
#
#     return render(request, 'search/search_result.html', {
#         'search_query': search_query,
#         'search_results': search_results,
#     })
