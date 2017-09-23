from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape, mark_safe

from django_comments_xtd.templatetags.comments_xtd import xtd_comment_gravatar_url

from wagtail.wagtailcore.models import Page

from copy import deepcopy

import markdown


register = template.Library()

@register.filter
def custom_xtd_comment_gravatar(email, size=48):
    url = xtd_comment_gravatar_url(email, size)
    return mark_safe('<img src="%s" height="%d" class="avatar avatar-42 photo" width="%d">' %
                     (url, size, size))


@register.filter(is_safe=True)
@stringfilter
def escape_space(value):
    return value.ljust(10).replace(' ', '&nbsp;')


@register.filter(name='markdown_code')
def markdown_code(value):
    value2 = deepcopy(value)
    return markdown.markdown(value2.value,
                                    extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',
                                    ])

query_dict = {
    '首页': 'home_page',
    '博客': 'blog',
    '联系': 'contact',
    '关于': 'about',
}

@register.simple_tag(takes_context=True)
def focus_text(context, value):
    current_name = query_dict[value]
    template_name = context.template_name.split('/')[-1]
    if current_name in template_name:
        return mark_safe('<font color="#d2691e">{}</font>'.format(value))
    return value


@register.inclusion_tag('blog/includes/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=2)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }