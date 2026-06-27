import datetime

from django.core.exceptions import ValidationError

from ratings.management.commands.base_tmdb_pull import BaseTmdbPullCommand
from ratings.models import People, TvCast, TvGenre, TvPage, TvIndexPage


class Command(BaseTmdbPullCommand):
    media_type = "tv"
    rated_media_type = "tv"
    page_model = TvPage
    index_page_model = TvIndexPage
    genre_model = TvGenre
    cast_model = TvCast
    people_model = People

    id_field = "tv_id"
    title_key = "name"
    date_key = "first_air_date"
    cast_relation = "tvcast_set"

    collection_name = "TV"
    log_filename = "pull_tv.log"
    algolia_index = "tv_index"
    command_label = "pull_tv"

    def save_media(self, media, index_page, poster_size):
        try:
            self._get_logger().info(f"Saving media: {media['name']}")
            child_page = TvPage(
                tv_id=media["id"],
                title=media["name"],
                description=media["overview"],
                release_date=datetime.datetime.strptime(
                    media["first_air_date"], "%Y-%m-%d"
                ).date(),
                rating=media["rating"],
                poster=(
                    "https://image.tmdb.org/t/p/" + poster_size + media["poster_path"]
                ),
                language=media["original_language"],
            )
            index_page.add_child(instance=child_page)
            child_page.genre.set(media["genre_ids"])
            child_page.save_revision().publish()
            self._get_logger().info(f"Media saved successfully: {media['name']}")

        except ValidationError:
            media_page = TvPage.objects.get(tv_id=media["id"])
            if media_page.rating != media["rating"]:
                media_page.rating = media["rating"]
                media_page.save_revision().publish()

            media_page.poster = (
                "https://image.tmdb.org/t/p/" + poster_size + media["poster_path"]
            )
            media_page.genre.set(media["genre_ids"])
            media_page.save_revision().publish()
