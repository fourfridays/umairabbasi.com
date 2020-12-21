# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from aldryn_django.utils import i18n_patterns
from django.views.generic import TemplateView
from wagtail.contrib.sitemaps.views import sitemap
import aldryn_addons.urls


urlpatterns = [
    url(r'^robots\.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^sitemap\.xml$', sitemap),
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
