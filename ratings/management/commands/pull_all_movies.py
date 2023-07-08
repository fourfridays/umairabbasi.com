import datetime, os, pathlib, requests

from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from django.core.files.images import ImageFile

from wagtail.models import Collection
from wagtail.images.models import Image

from ratings.models import MoviesIndexPage, MoviePage

from io import BytesIO


class Command(BaseCommand):
    def save_media(self, media, movies_index_page, poster_size):
        try:
            child_page = MoviePage(
                tmdb_id=media["id"],
                title=media["title"],
                description=media["overview"],
                release_date=datetime.datetime.strptime(
                    media["release_date"], "%Y-%m-%d"
                ).date(),
                rating=media["rating"],
                poster="https://image.tmdb.org/t/p/"
                + poster_size
                + media["poster_path"],
                language=media["original_language"],
            )
            movies_index_page.add_child(instance=child_page)
            child_page.save()

        except ValidationError:
            media_page = MoviePage.objects.get(tmdb_id=media["id"])
            # if we updated our rating for an existing media in Wagtail
            if media_page.rating != media["rating"]:
                media_page.rating = media["rating"]
                media_page.save_revision().publish()
            else:
                pass

            # if we updated poster size for an existing poster path in Wagtail
            media_page.poster = (
                "https://image.tmdb.org/t/p/" + poster_size + media["poster_path"]
            )
            media_page.save()

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

    def handle(self, *args, **options):
        # Check to see if MovieIndexPage exists
        movies_index_page = MoviesIndexPage.objects.live().public().get()

        # Get movies rated by user if movies_index_page exists
        if movies_index_page:
            print("Pulling Movies")

            page_number = 1
            account_id = os.getenv("TMDB_ACCOUNT_ID").strip('""').strip("''")
            api_key = os.getenv("TMDB_API_KEY").strip('""').strip("''")
            session_id = os.getenv("TMDB_SESSION_ID").strip('""').strip("''")
            headers = {"accept": "application/json"}
            response = requests.get(f"https://api.themoviedb.org/3/account/{account_id}/rated/movies?api_key={api_key}&language=en-US&session_id={session_id}&sort_by=created_at.desc&page={page_number}, headers={headers}")
            json_results = response.json()
            total_pages = json_results["total_pages"]
            poster_size = "w500"

            while page_number <= total_pages:
                response = requests.get(f"https://api.themoviedb.org/3/account/{account_id}/rated/movies?api_key={api_key}&language=en-US&session_id={session_id}&sort_by=created_at.desc&page={page_number}")
                json_results = response.json()

                for media in json_results["results"]:
                    self.save_media(media, movies_index_page, poster_size)

                page_number += 1

            print("Pulling Movie Posters")
            movies = MoviePage.objects.live().public().all()
            collection = Collection.objects.get(name="Movies")
            for movie in movies:
                if not movie.image:
                    self.get_poster(movie, collection)
