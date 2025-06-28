import os

from django.shortcuts import render
from django.views import View

from ratings.models import MoviePage, People, TvPage


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


class CastView(View):
    template_name = "ratings/cast.html"

    def get(self, request, *args, **kwargs):
        person_id = kwargs.get("people_id")
        person = People.objects.get(id=person_id)
        movies = (
            MoviePage.objects.filter(
                cast__cast_member__id=person_id)
                .distinct()
                .order_by("-release_date")
        )
        tv_shows = (
            TvPage.objects.filter(
                tvcast__cast_member__id=person_id)
                .distinct()
                .order_by("-release_date")
        )
        context = {
            "person": person,
            "movies": movies,
            "tv_shows": tv_shows,
        }
        return render(request, self.template_name, context)
