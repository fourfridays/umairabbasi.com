import os
import time

from django.core.management.base import BaseCommand
from algoliasearch.search_client import SearchClient
from ratings.models import TvPage


class Command(BaseCommand):
    def handle(self, *args, **options):
        algolia_app_id = os.environ.get("ALGOLIA_APP_ID", "")
        algolia_api = os.environ.get("ALGOLIA_API", "")
        client = SearchClient.create(algolia_app_id, algolia_api)
        index = client.init_index("tv_index")

        tv_shows = TvPage.objects.live().all()

        for tv_show in tv_shows:
            tv_index = {}
            tv_index = {
                "objectID": tv_show.tv_id,
                "title": tv_show.title,
                "description": tv_show.description,
                "language": tv_show.language,
                "release_date_timestamp": time.mktime(tv_show.release_date.timetuple()),
                "release_year": tv_show.release_date.year,
                "rating": tv_show.rating,
                "poster": tv_show.poster,
                "genre": list(tv_show.genre.values_list("name", flat=True)),
                "cast": list(
                    tv_show.tvcast_set.values_list("cast_member__name", flat=True)
                ),
                "url": tv_show.url,
            }
            index.save_object(tv_index)
