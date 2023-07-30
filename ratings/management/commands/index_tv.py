import os

from django.core.management.base import BaseCommand
from algoliasearch.search_client import SearchClient
from ratings.models import TvPage


class Command(BaseCommand):
    def handle(self, *args, **options):
        algolia_app_id = os.environ.get("ALGOLIA_APP_ID", "")
        algolia_api = os.environ.get("ALGOLIA_API", "")
        client = SearchClient.create(algolia_app_id, algolia_api)
        index = client.init_index('tv_index')

        tv_shows = TvPage.objects.live().all()

        for tv_show in tv_shows:
            tv_index = {}
            tv_index = {
                "objectID": tv_show.tv_id,
                "Title": tv_show.title,
                "Description": tv_show.description,
                "Release Year": tv_show.release_date.year,
                "Rating": tv_show.rating,
                "Poster": tv_show.poster,
                "Genre": list(tv_show.genre.values_list("name", flat=True)),
                "Cast": list(tv_show.tvcast_set.values_list("cast_member__name", flat=True)),
            }
            index.save_object(tv_index)
