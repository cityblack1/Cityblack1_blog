from record.models import UserAction, PageRecord, UserSearchRecord
from collections import namedtuple

from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser
import re

UrlTitle = namedtuple('UrlTitle', 'login logout register')
url_title = UrlTitle('登录', '登出', '注册')


class RecordMiddleWare(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
        super(RecordMiddleWare, self).__init__(*args, **kwargs)
        self.is_wagtail = False

    def process_response(self, request, response):
        url = request.path
        if url.startswith('/search/'):
            user = None if isinstance(request.user, AnonymousUser) else request.user
            url = request.path
            ip_address = request.META['REMOTE_ADDR']
            content_object = None
            try:
                title = content_object.title
            except:
                try:
                    html = response.content
                    title = re.search(b'title.*?>(.*?)<', html, flags=re.S).group(1).decode('utf-8')
                except:
                    title = ''
            user_action = UserAction(user=user, url=url, ip_address=ip_address, content_object=content_object,
                                     title=title)
            user_action.save()
            return response
        if request.method == 'GET' and request.is_ajax():
            return response
        if request.method == 'POST':
            request.META['has_post'] = True
            if url.startswith('/users/'):
                user = None if isinstance(request.user, AnonymousUser) else request.user
                if user is None:
                    return response
                ip_address = request.META['REMOTE_ADDR']
                content_object = None
                title = getattr(url_title, url.split('/')[-2])
                user_action = UserAction(user=user, url=url, ip_address=ip_address, content_object=content_object,
                                         title=title)
                user_action.save()
        return response

    def process_template_response(self, request, response):
        try:
            if 'page' in response.context_data and 'self' in response.context_data:
                self.is_wagtail = True
            else:
                self.is_wagtail = False
        except:
            return response
        if self.is_wagtail:
            user = None if isinstance(request.user, AnonymousUser) else request.user
            url = request.path
            ip_address = request.META['REMOTE_ADDR']
            content_object = response.context_data['page']
            try:
                title = content_object.title
            except:
                try:
                    html = str(response.rendered_content)
                    title = re.search('title.*?>(.*?)<', html, flags=re.S).group(1)
                except:
                    title = ''
            user_action = UserAction(user=user, url=url, ip_address=ip_address, content_object=content_object, title=title)
            user_action.save()
        return response

    def process_request(self, request):
        url = request.path
        if request.method == 'GET' and request.is_ajax():
            return None
        if request.method == 'POST':
            request.META['has_post'] = True
            if url.startswith('/users/'):
                user = None if isinstance(request.user, AnonymousUser) else request.user
                if user is None:
                    return None
                ip_address = request.META['REMOTE_ADDR']
                content_object = None
                title = getattr(url_title, url.split('/')[-2])
                user_action = UserAction(user=user, url=url, ip_address=ip_address, content_object=content_object,
                                         title=title)
                user_action.save()
        return None
