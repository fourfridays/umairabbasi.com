import os
import time

from django.core.management.base import BaseCommand
from algoliasearch.search_client import SearchClient
from ratings.models import MoviePage


class Command(BaseCommand):
    def handle(self, *args, **options):
        algolia_app_id = os.environ.get("ALGOLIA_APP_ID", "")
        algolia_api = os.environ.get("ALGOLIA_SEARCH_API", "")
        client = SearchClient.create(algolia_app_id, algolia_api)
        index = client.init_index("movie_index")

        movies = MoviePage.objects.live().all()

        for movie in movies:
            movie_index = {}
            movie_index = {
                "objectID": movie.movie_id,
                "title": movie.title,
                "description": movie.description,
                "language": movie.language,
                "release_date_timestamp": time.mktime(movie.release_date.timetuple()),
                "release_year": movie.release_date.year,
                "rating": movie.rating,
                "poster": movie.poster,
                "genre": list(movie.genre.values_list("name", flat=True)),
                "cast": list(
                    movie.cast_set.values_list("cast_member__name", flat=True)
                ),
                "url": movie.url,
            }
            index.save_object(movie_index)
