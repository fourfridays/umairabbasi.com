from django.db import models
from django.shortcuts import redirect, render
from django.template.defaultfilters import slugify

from wagtail.core.models import Page
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.search import index


class MoviesIndexPage(Page):
    pass