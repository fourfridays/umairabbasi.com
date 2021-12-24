from django.db import models
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from page.blocks import PersonDateBlock


class MoviePage(Page):
    parent_page_types = ['MoviesIndexPage']
    description = models.TextField()
    release_date = models.CharField(max_length=10, blank=True)
    rating = models.IntegerField(blank=True)
    poster = models.URLField(blank=True)
    language = models.CharField(max_length=2, blank=True)
    tmdb_id = models.IntegerField(unique=True, default=None)
    watch_party = StreamField([
        ('view_block', PersonDateBlock()),
    ], default='', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('release_date'),
        FieldPanel('rating'),
        FieldPanel('poster'),
        FieldPanel('language'),
        FieldPanel('tmdb_id'),
        StreamFieldPanel('watch_party'),
    ]


class MoviesIndexPage(RoutablePageMixin, Page):
    subpage_types = ['MoviePage']

    def get_context(self, request):
        context = super(MoviesIndexPage, self).get_context(request)
        context['movie_pages'] = MoviePage.objects.live().filter(rating__gte=7).order_by('-rating', '-release_date')
        context['count'] = context['movie_pages'].count()
        return context

    @route(r'^all/$')
    def get_all_movies(self, request):
        context = super(MoviesIndexPage, self).get_context(request)
        context['movies'] = MoviePage.objects.live().order_by('title')
        context['count'] = context['movies'].count()
        return render(request, 'ratings/get_all_movies.html', context)


class TvPage(Page):
    parent_page_types = ['TvIndexPage']
    description = models.TextField()
    release_date = models.CharField(max_length=10, blank=True)
    rating = models.IntegerField(blank=True)
    poster = models.URLField(blank=True)
    language = models.CharField(max_length=2, blank=True)
    tmdb_id = models.IntegerField(unique=True, default=None)
    watch_party = StreamField([
        ('view_block', PersonDateBlock()),
    ], default='', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('release_date'),
        FieldPanel('rating'),
        FieldPanel('poster'),
        FieldPanel('language'),
        FieldPanel('tmdb_id'),
        StreamFieldPanel('watch_party'),
    ]


class TvIndexPage(RoutablePageMixin, Page):
    subpage_types = ['TvPage']

    def get_context(self, request):
        context = super(TvIndexPage, self).get_context(request)
        context['tv_pages'] = TvPage.objects.live().filter(rating__gte=7).order_by('-rating', '-release_date')
        context['count'] = context['tv_pages'].count()
        return context

    @route(r'^all/$')
    def get_all_tv_shows(self, request):
        context = super(TvIndexPage, self).get_context(request)
        context['tv_shows'] = TvPage.objects.live().order_by('title')
        context['count'] = context['tv_shows'].count()
        return render(request, 'ratings/get_all_tv_shows.html', context)


class RatingsIndexPage(Page):

    def get_context(self, request):
        context = super(RatingsIndexPage, self).get_context(request)
        context['movie_page'] = MoviePage.objects.get(title='Layer Cake')
        return context