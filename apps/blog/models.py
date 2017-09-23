from django.db import models
from django.contrib.contenttypes.models import ContentType
from .views import recommend_articles

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailsearch import index
from wagtail.wagtailadmin.edit_handlers import *
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from record.models import PageRecord
from mycomment.models import MyComment
from .fields import DemoStreamBlock, LinkFields, RelatedLink, BlogIndexPageRelatedLink, \
    BlogPagePageCoverItem, BlogPageRelatedLink, BlogPageTag

from django.db.models import F


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    subpage_types = ['blog.BlogPage']

    @property
    def get_blogs(self):
        # 得到这个索引页面下的全部Blog子页面
        blogs = BlogPage.objects.live().descendant_of(self)
        blogs = blogs.order_by('-first_published_at')
        return blogs

    def get_context(self, request, *args, **kwargs):
        context = super(BlogIndexPage, self).get_context(request)
        context['blogs'] = self.get_blogs
        return context

BlogIndexPage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('intro', classname='full'),
    InlinePanel('related_links', label='Related links')
]

BlogIndexPage.promote_panels = Page.promote_panels


# blog 页面
class BlogPage(Page):
    body = StreamField(DemoStreamBlock())
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    date = models.DateField('Post Date')
    read_times = models.IntegerField(default=0, verbose_name='阅读次数', blank=True, null=True)
    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='添加显示在首页的封面图',
        verbose_name='封面图'
    )

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []

    search_fields =[
        index.SearchField('title', partial_match=True, boost=2),
        index.FilterField('live'),
    ]

    def __str__(self):
        return self.title

    def get_port_url(self, request=None):
        url_parts = self._safe_get_url_parts(request=request)

        if url_parts is None:
            # page is not routable
            return

        site_id, root_url, page_path = url_parts
        return root_url

    def get_absolute_url(self, request=None):
        url_parts = self._safe_get_url_parts(request=request)

        if url_parts is None:
            # page is not routable
            return

        site_id, root_url, page_path = url_parts

        return page_path

    def parent(self):
        parent = self.get_parent().specific
        return parent

    def get_context(self, request, *args, **kwargs):
        similar_blog = recommend_articles(self)
        if self.first_published_at:
            try:
                blog_page = self.blog_page
            except:
                blog_page = PageRecord.objects.create(blog_page=self)
            blog_page.visit_times = F('visit_times') + 1
            blog_page.save()

        from utils.custom_context.blog_context import reset_data
        reset_data()
        context = super(BlogPage, self).get_context(request)
        context['similar_blog'] = similar_blog
        return context

    def save(self, *args, **kwargs):
        from utils.custom_context.blog_context import reset_data
        reset_data()
        super(BlogPage, self).save(*args, **kwargs)


BlogPage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('date'),
    StreamFieldPanel('body'),
]
BlogPage.promote_panels = Page.promote_panels + [
    FieldPanel('tags'),
    ImageChooserPanel('cover_image'),
    InlinePanel('related_links', label="相关网页"),
]

# """
# feed_image = models.ForeignKey(
#         'wagtailimages.Image',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+'
#     )
#
#
# InlinePanel('page_cover_item', label='轮播图'),
#
class AboutPage(Page):
    body = StreamField(DemoStreamBlock())
AboutPage.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body'),
]
AboutPage.promote_panels = Page.promote_panels


