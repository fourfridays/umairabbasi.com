from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel

from blog.models import PullQuoteBlock, ImageFormatChoiceBlock, HTMLAlignmentChoiceBlock, ImageBlock, AlignedHTMLBlock, BlogStreamBlock

class Home(Page):
    body = StreamField ([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('rawhtml', blocks.RawHTMLBlock()),
    ])

Home.content_panels = [
    StreamFieldPanel('body'),
]

class Bootstrap12(Page):
    body = StreamField(BlogStreamBlock())

    class Meta:
        verbose_name = _('Bootstrap 12 Column')

Bootstrap12.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body'),
]
