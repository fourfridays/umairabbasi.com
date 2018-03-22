from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks

from wagtail.admin.edit_handlers import StreamFieldPanel 

from wagtail.core.blocks import TextBlock, StructBlock, StreamBlock, CharBlock, URLBlock
from wagtail.images.blocks import ImageChooserBlock


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

