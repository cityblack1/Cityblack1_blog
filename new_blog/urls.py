from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.i18n import JavaScriptCatalog
from django.views.static import serve

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from new_blog.settings.base import MEDIA_ROOT
from search import views as search_views
from users import urls as user_urls
from api import urls as api_urls
from mycomment.views import like




urlpatterns = [
    url(r'^comments/like/(\d+)/$', like, name='comments-xtd-like'),

    url(r'^comments/', include('django_comments_xtd.urls')),

    url(r'^record/', include('record.urls', namespace='访问记录')),

    url(r'^feedback/', include('mycomment.urls')),

    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^users/', include(user_urls, namespace='users')),

    url(r'^api/', include(api_urls, namespace='api')),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', includes(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
