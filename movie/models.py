from django.db import models
from django.shortcuts import redirect, render
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from django.template.defaultfilters import slugify
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.search import index
from page.blocks import ViewDateBlock

class Movie(models.Model):
    title = models.TextField(unique=True)
    slug = models.SlugField(max_length=120, unique=True, null=True, blank=True)
    view_date = StreamField(ViewDateBlock(required=False), default='', blank=True)
    overview = models.TextField()
    release_date = models.CharField(max_length=10, blank=True)
    rating = models.IntegerField(blank=True)
    poster = models.URLField(blank=True)
    language = models.CharField(max_length=2, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            count = Movie.objects.filter(slug=slug).count()
            if count > 0:
                slug = '{}-{}'.format(slug, count)
            self.slug = slug
        return super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        """String for representing the object in Admin site otherwise it just shows object in program requisite group id"""
        return self.title

    class Meta:
        ordering = ["title"]

    panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
        StreamFieldPanel('view_date'),
    ]


class MoviesIndexPage(RoutablePageMixin, Page):
    def get_movies(self):
        movies = Movie.objects.all().order_by('title')
        return movies

    @route("^$")
    def get_all_movies(self, request):
        context = super().get_context(request)
        context['movies'] = self.get_movies()
        context['count'] = context['movies'].count()
        return render(request, 'movie/movies_index_page.html', context)

    @route(r'^top-rated/$')
    def get_top_rated_movies(self, request):
        context = super().get_context(request)
        context['top_rated'] = self.get_movies().filter(rating__gte = 8).order_by('title')
        context['count'] = context['top_rated'].count()
        
        return render(request, 'movie/top_rated.html', context)

    @route(r'^movie/(?P<slug>[-\w]+)/$')  
    def get_movie(self, request, slug):
        context = super().get_context(request)
        context['movie'] = self.get_movies().get(slug=slug)
        
        return render(request, 'movie/movie.html', context)

    def get_sitemap_urls(self, request):
        sitemap = []
        movies = self.get_movies()
        for movie in movies:
            data = {
                'location': self.full_url + movie.slug + '/',
                'changefreq': 'daily',
            }
            sitemap.append(data)
        return sitemap