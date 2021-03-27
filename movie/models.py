from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.search import index


class MoviesIndexPage(Page):
    pass