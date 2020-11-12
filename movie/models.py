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
    creation_date = models.DateField(null=True, blank=True) 

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            count = Movie.objects.filter(slug=slug).count()
            if count > 0:
                slug = '{}-{}'.format(slug, count)
            self.slug = slug
        return super(Movie, self).save(*args, **kwargs)


class MoviesIndexPage(RoutablePageMixin, Page):
    def get_movies(self):
        movies = Movie.objects.all().order_by('-creation_date')
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
        context['top_rated'] = self.get_movies().filter(rating__gte = 8).order_by('-rating')
        context['count'] = context['top_rated'].count()
        
        return render(request, 'movie/top_rated.html', context)

    @route(r'^movie/(?P<slug>[-\w]+)/$')  
    def get_movie(self, request, slug):
        context = super().get_context(request)
        context['movie'] = self.get_movies().get(slug=slug)
        
        return render(request, 'movie/movie.html', context)