from wagtail.wagtailcore.blocks import *
from wagtail.wagtailimages.blocks import *
from wagtail.wagtaildocs.blocks import *
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailsearch import index
from wagtail.wagtailadmin.edit_handlers import *
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from modelcluster.tags import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase

from django import forms
from django.db import models





# 一个包含了若干字段的抽象类，用于一些model继承
class LinkFields(models.Model):
    link_external = models.URLField('拓展链接', blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        verbose_name='相关页面'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+',
        verbose_name='相关文件'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document')
    ]

    class Meta:
        abstract = True


# 在抽象类LinkFields的基础上对一些字段进行拓展，并重新定义panels
class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text='link title')

    # 使用MultiFieldPanel定义混合字段
    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "link")
    ]

    # 仍然定义为抽象类，让后面的model去继承
    class Meta:
        abstract = True


# Blog的索引页面


# 定义一个Orderable，让后面的InlineField引用
class BlogIndexPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('blog.BlogIndexPage', related_name='related_links')



class PullQuoteBlock(StructBlock):
    quote = TextBlock("quote title")
    attribution = CharBlock()

    class Meta:
        icon = "openquote"


class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('small', '小尺寸(300)'), ('full', '全框'),
    ))


class HTMLAlignmentChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('normal', 'Normal'), ('full', 'Full width'),
    ))


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = RichTextBlock(required=False)
    alignment = ImageFormatChoiceBlock()


class AlignedHTMLBlock(StructBlock):
    html = RawHTMLBlock()
    alignment = HTMLAlignmentChoiceBlock()

    class Meta:
        icon = "code"


class DemoStreamBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title", label="测试")
    h3 = CharBlock(icon="title", classname="title")
    h4 = CharBlock(icon="title", classname="title")
    paragraph = RichTextBlock(icon="pilcrow")
    aligned_image = ImageBlock(label="Aligned image", icon="image")
    pullquote = PullQuoteBlock()
    document = DocumentChooserBlock(icon="doc-full-inverse")
    markdown = TextBlock(icon="code")




# 封面轮播图, 这个功能只对特定页面有效
class PageCoverItem(LinkFields):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='相关图片'
    )

    panels = [
        ImageChooserPanel('image'),
        MultiFieldPanel(LinkFields.panels, "link")
    ]


class BlogPagePageCoverItem(Orderable, PageCoverItem):
    page = ParentalKey('blog.BlogPage', related_name='page_cover_item')


# 相关链接
class BlogPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('blog.BlogPage', related_name='related_links')


# django插件taggit的集成
class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('blog.BlogPage', related_name='taggit_items')















