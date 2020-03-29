from django.db import models
from django.shortcuts import redirect, render
from wagtail.core.models import Page
from django.template.defaultfilters import slugify
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.search import index


class Movie(models.Model):
    title = models.TextField(unique=True)
    slug = models.SlugField(max_length=120, unique=True, null=True, blank=True)
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


class MoviesIndexPage(RoutablePageMixin, Page):
    @route("^$")
    def get_movies(self, request):
        context = super().get_context(request)
        context['movies'] = Movie.objects.all().order_by('title')
        return render(request, 'movie/movies_index_page.html', context)

    @route(r'^movie/(?P<slug>[-\w]+)/$')  
    def get_movie(self, request, slug):
        context = super().get_context(request)
        context['movie'] = Movie.objects.all().get(slug=slug)
        return render(request, 'movie/movie.html', context)