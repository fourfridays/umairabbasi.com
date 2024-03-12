import os

from django.shortcuts import render
from django.views import View

from ratings.models import MoviePage, MoviesIndexPage, TvPage, TvIndexPage


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
