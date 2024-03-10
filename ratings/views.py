import os

from django.shortcuts import render
from django.views import View

from ratings.models import *


class MovieIndexView(View):
    template_name = "ratings/movies_index_page.html"

    def get(self, request, *args, **kwargs):
        context = self.set_search_context()
        return render(request, self.template_name, context)

    def set_search_context(self):
        context = {
            "algolia_app_id": os.environ.get("ALGOLIA_APP_ID", ""),
            "algolia_search_api": os.environ.get("ALGOLIA_SEARCH_API", ""),
        }

        return context


class TvIndexView(View):
    template_name = "ratings/tv_index_page.html"

    def get(self, request, *args, **kwargs):
        context = self.set_search_context()
        return render(request, self.template_name, context)

    def set_search_context(self):
        context = {
            "algolia_app_id": os.environ.get("ALGOLIA_APP_ID", ""),
            "algolia_search_api": os.environ.get("ALGOLIA_SEARCH_API", ""),
        }

        return context


def movie_search(request):
    search_query = request.GET.get("query", None)
    if search_query:
        search_results = MoviePage.objects.live().search(search_query)
        movie_count = MoviesIndexPage.get_movie_count(request, search_results)

        return render(
            request,
            "ratings/movies_index_page.html",
            {
                "title": "Movie Search Results",
                "search_query": search_query,
                "movie_count": movie_count,
                "media": search_results,
            },
        )
    else:
        search_results = MoviePage.objects.live().order_by("title")

    # Render template
    return render(
        request,
        "ratings/movies_index_page.html",
        {
            "media": search_results,
        },
    )


def tv_search(request):
    search_query = request.GET.get("query", None)
    if search_query:
        search_results = TvPage.objects.live().search(search_query)
        tv_count = TvIndexPage.get_tv_count(request, search_results)

        return render(
            request,
            "ratings/tv_index_page.html",
            {
                "title": "TV Show Search Results",
                "search_query": search_query,
                "tv_count": tv_count,
                "media": search_results,
            },
        )
    else:
        search_results = TvPage.objects.live().order_by("title")

    # Render template
    return render(
        request,
        "ratings/tv_index_page.html",
        {
            "media": search_results,
        },
    )
