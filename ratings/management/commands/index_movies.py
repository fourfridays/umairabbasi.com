import os

from django.core.management.base import BaseCommand
from algoliasearch.search_client import SearchClient
from ratings.models import MoviePage


class Command(BaseCommand):
    def handle(self, *args, **options):
        algolia_app_id = os.environ.get("ALGOLIA_APP_ID", "")
        algolia_api = os.environ.get("ALGOLIA_API", "")
        client = SearchClient.create(algolia_app_id, algolia_api)
        index = client.init_index('movie_index')

        movies = MoviePage.objects.live().all()

        for movie in movies:
            movie_index = {}
            movie_index = {
                "objectID": movie.movie_id,
                "Title": movie.title,
                "Description": movie.description,
                "Release Year": movie.release_date.year,
                "Rating": movie.rating,
                "Poster": movie.poster,
                "Genre": list(movie.genre.values_list("name", flat=True)),
                "Cast": list(movie.cast_set.values_list("cast_member__name", flat=True)),
            }
            index.save_object(movie_index)
