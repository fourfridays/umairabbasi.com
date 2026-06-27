import datetime

from django.core.exceptions import ValidationError

from ratings.management.commands.base_tmdb_pull import BaseTmdbPullCommand
from ratings.models import Cast, MovieGenre, MoviePage, MoviesIndexPage, People


class Command(BaseTmdbPullCommand):
    media_type = "movie"
    page_model = MoviePage
    index_page_model = MoviesIndexPage
    genre_model = MovieGenre
    cast_model = Cast
    people_model = People

    id_field = "movie_id"
    title_key = "title"
    date_key = "release_date"
    cast_relation = "cast_set"

    collection_name = "Movies"
    log_filename = "pull_movies.log"
    algolia_index = "movie_index"
    command_label = "pull_movies"

    def save_media(self, media, index_page, poster_size):
        try:
            self._get_logger().info(f"Saving media: {media['title']}")
            child_page = MoviePage(
                movie_id=media["id"],
                title=media["title"],
                description=media["overview"],
                release_date=datetime.datetime.strptime(
                    media["release_date"], "%Y-%m-%d"
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
            self._get_logger().info(f"Media saved successfully: {media['title']}")

        except ValidationError:
            media_page = MoviePage.objects.get(movie_id=media["id"])
            if media_page.rating != media["rating"]:
                media_page.rating = media["rating"]
                media_page.save_revision().publish()

            media_page.poster = (
                "https://image.tmdb.org/t/p/" + poster_size + media["poster_path"]
            )
            media_page.genre.set(media["genre_ids"])
            media_page.save_revision().publish()
