import datetime
import logging
import os
import pathlib
import time

import requests
from algoliasearch.search.client import SearchClientSync
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from io import BytesIO
from wagtail.images.models import Image
from wagtail.models import Collection


class BaseTmdbPullCommand(BaseCommand):
    """Shared base for pull_movies and pull_tv management commands."""

    # --- Subclass overrides ---------------------------------------------------
    media_type = "movie"              # used in TMDB API paths ("movie" | "tv")
    rated_media_type = "movies"        # used in /rated/ endpoint ("movies" | "tv")
    page_model = None             # MoviePage | TvPage
    index_page_model = None       # MoviesIndexPage | TvIndexPage
    genre_model = None            # MovieGenre | TvGenre
    cast_model = None             # Cast | TvCast
    people_model = None           # People (shared, but kept for symmetry)

    id_field = "movie_id"         # "movie_id" | "tv_id"
    title_key = "title"           # API key for media title ("title" | "name")
    date_key = "release_date"     # API key for release ("release_date" | "first_air_date")
    cast_relation = "cast_set"    # reverse FK on page_model ("cast_set" | "tvcast_set")

    collection_name = "Movies"
    log_filename = "pull_movies.log"
    algolia_index = "movie_index"
    command_label = "pull_movies"

    # --- Logging setup --------------------------------------------------------
    logger = None

    def _get_logger(self):
        if self.logger is None:
            self.logger = logging.getLogger(self.command_label)
            if not self.logger.handlers:
                self.logger.setLevel(logging.INFO)
                self.logger.addHandler(logging.StreamHandler())
                self.logger.addHandler(logging.FileHandler(self.log_filename))
        return self.logger

    # --- Shared helpers -------------------------------------------------------
    def _tmdb_headers(self):
        return {"accept": "application/json"}

    @staticmethod
    def _tmdb_env():
        return {
            "account_id": os.getenv("TMDB_ACCOUNT_ID", "").strip('""').strip("''"),
            "api_key": os.getenv("TMDB_API_KEY", "").strip('""').strip("''"),
            "session_id": os.getenv("TMDB_SESSION_ID", "").strip('""').strip("''"),
        }

    def _tmdb_get(self, url):
        response = requests.get(url, headers=self._tmdb_headers())
        response.raise_for_status()
        return response.json()

    def _fetch_genres(self, api_key, session_id):
        data = self._tmdb_get(
            f"https://api.themoviedb.org/3/genre/{self.media_type}/list"
            f"?api_key={api_key}&language=en-US&session_id={session_id}"
        )
        for genre in data["genres"]:
            self.genre_model.objects.update_or_create(
                id=genre["id"],
                name=genre["name"],
            )

    def _fetch_rated_pages(self, account_id, api_key, session_id):
        """Return (first_page_json, total_pages) or abort early."""
        url = (
            f"https://api.themoviedb.org/3/account/{account_id}/rated/{self.rated_media_type}"
            f"?api_key={api_key}&language=en-US&session_id={session_id}"
            f"&sort_by=created_at.desc&page=1"
        )
        data = self._tmdb_get(url)
        if "total_pages" not in data:
            self._get_logger().warning(
                "API response missing 'total_pages'; aborting pull."
            )
            return None, 0
        return data, data["total_pages"]

    def _paginate_rated(self, account_id, api_key, session_id, page):
        url = (
            f"https://api.themoviedb.org/3/account/{account_id}/rated/{self.rated_media_type}"
            f"?api_key={api_key}&language=en-US&session_id={session_id}"
            f"&sort_by=created_at.desc&page={page}"
        )
        return self._tmdb_get(url)

    def _fetch_credits(self, media_id, api_key, session_id):
        url = (
            f"https://api.themoviedb.org/3/{self.media_type}/{media_id}/credits"
            f"?api_key={api_key}&language=en-US&session_id={session_id}"
        )
        return self._tmdb_get(url)

    # --- Persistence helpers --------------------------------------------------
    def save_people(self, person):
        self.people_model.objects.update_or_create(
            id=person["id"],
            name=person["name"],
        )

    def save_cast(self, cast_results):
        for person in cast_results["cast"]:
            try:
                self.cast_model.objects.update_or_create(
                    **{self.media_type: self.page_model.objects.get(**{self.id_field: cast_results["id"]})},
                    cast_member=self.people_model.objects.get(id=person["id"]),
                    character=person["character"],
                )
            except ObjectDoesNotExist:
                self.save_people(person)
                self.cast_model.objects.update_or_create(
                    **{self.media_type: self.page_model.objects.get(**{self.id_field: cast_results["id"]})},
                    cast_member=self.people_model.objects.get(id=person["id"]),
                    character=person["character"],
                )

    def media_exists(self, media_id):
        try:
            self.page_model.objects.get(**{self.id_field: media_id})
            return True
        except ObjectDoesNotExist:
            return False

    def get_poster(self, media, collection):
        response = requests.get(media.poster)
        filename = pathlib.Path(media.poster).name

        media_image = Image(
            title=media.title,
            file=ImageFile(BytesIO(response.content), name=filename),
            collection_id=collection.id,
        )
        media_image.save()
        media_image.tags.add("poster")
        media.image = media_image
        media.save()

    def index_media(self, item):
        algolia_app_id = os.environ.get("ALGOLIA_APP_ID", "")
        algolia_api = os.environ.get("ALGOLIA_API", "")
        client = SearchClientSync(algolia_app_id, algolia_api)

        cast_field = getattr(item, self.cast_relation)
        media_index = {
            "objectID": getattr(item, self.id_field),
            "title": item.title,
            "description": item.description,
            "language": item.language,
            "release_date_timestamp": time.mktime(item.release_date.timetuple()),
            "release_year": item.release_date.year,
            "rating": item.rating,
            "poster": item.poster,
            "genre": list(item.genre.values_list("name", flat=True)),
            "cast": list(cast_field.values_list("cast_member__name", flat=True)),
            "url": item.url,
        }
        client.save_object(index_name=self.algolia_index, body=media_index)

    # --- Subclass hook --------------------------------------------------------
    def save_media(self, media, index_page, poster_size):
        """Create or update a single media page. Must be overridden by subclasses."""
        raise NotImplementedError

    # --- Main handle ----------------------------------------------------------
    def handle(self, *args, **options):
        now = datetime.datetime.now()
        log = self._get_logger()
        log.info(f"Starting the {self.command_label} command: {now}")

        index_page = self.index_page_model.objects.live().public().get()
        if not index_page:
            return

        env = self._tmdb_env()
        api_key = env["api_key"]
        session_id = env["session_id"]
        account_id = env["account_id"]

        # Genres
        self._fetch_genres(api_key, session_id)

        # Rated media — first page
        first_page, total_pages = self._fetch_rated_pages(account_id, api_key, session_id)
        if first_page is None:
            return

        poster_size = "w500"

        # Process first page inline, then paginate the rest
        for media in first_page["results"]:
            self._process_media(media, index_page, poster_size, api_key, session_id)

        page_number = 2
        while page_number <= total_pages:
            data = self._paginate_rated(account_id, api_key, session_id, page_number)
            for media in data["results"]:
                self._process_media(media, index_page, poster_size, api_key, session_id)
            page_number += 1

        # Post-processing: posters + indexing
        items = self.page_model.objects.live().public().all()
        collection = Collection.objects.get(name=self.collection_name)
        for item in items:
            if not item.image:
                log.info(f"Fetching poster for {self.media_type}: {item.title}")
                self.get_poster(item, collection)

            if not settings.DEBUG:
                self.index_media(item)

        end = datetime.datetime.now()
        log.info(f"Finished the {self.command_label} command: {end}. Duration: {end - now}")

    def _process_media(self, media, index_page, poster_size, api_key, session_id):
        if self.media_exists(media["id"]):
            page = self.page_model.objects.get(**{self.id_field: media["id"]})
            if page.rating != media["rating"]:
                page.rating = media["rating"]
                page.save_revision().publish()
        else:
            self.save_media(media, index_page, poster_size)
            cast_results = self._fetch_credits(media["id"], api_key, session_id)
            if cast_results.get("cast"):
                self.save_cast(cast_results)
