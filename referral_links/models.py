from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks

from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel 

from wagtail.wagtailcore.blocks import TextBlock, StructBlock, StreamBlock, CharBlock, URLBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class ReferralBlock(StructBlock):
    title = CharBlock(classname='title')
    description = TextBlock()
    image = ImageChooserBlock(required=False)
    link = URLBlock()


class ReferralLinks(Page):
    body = StreamField([
        ('referral', ReferralBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

