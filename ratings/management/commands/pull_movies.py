import datetime, os, pathlib, requests

from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.files.images import ImageFile

from wagtail.models import Collection
from wagtail.images.models import Image

from ratings.models import Cast, MoviesIndexPage, MoviePage, MovieGenre, People

from io import BytesIO


class Command(BaseCommand):
    def save_media(self, media, movies_index_page, poster_size):
        try:
            child_page = MoviePage(
                movie_id=media["id"],
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

            # Setting genre
            child_page.genre.set(media["genre_ids"])

            child_page.save()

        except ValidationError:
            media_page = MoviePage.objects.get(movie_id=media["id"])
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

            # Setting genre
            media_page.genre.set(media["genre_ids"])

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

    def save_people(self, person):
        People.objects.update_or_create(
            id=person["id"],
            name=person["name"],
        )

    def save_cast(self, cast_results):
        for person in cast_results["cast"]:
            try:
                Cast.objects.update_or_create(
                    movie=MoviePage.objects.get(movie_id=cast_results["id"]),
                    cast_member=People.objects.get(id=person["id"]),
                    character=person["character"],
                )
            except ObjectDoesNotExist:
                # Fetch people from person API
                # See https://developer.themoviedb.org/reference/person-details
                self.save_people(person)

                # Try updating the Cast again
                Cast.objects.update_or_create(
                    movie=MoviePage.objects.get(movie_id=cast_results["id"]),
                    cast_member=People.objects.get(id=person["id"]),
                    character=person["character"],
                )

    def handle(self, *args, **options):
        def movie_exists(movie_id):
            try:
                MoviePage.objects.get(id=movie_id)
                return True
            except ObjectDoesNotExist:
                return False

        # Check to see if MovieIndexPage exists
        movies_index_page = MoviesIndexPage.objects.live().public().get()

        # Get movies rated by user if movies_index_page exists
        if movies_index_page:
            page_number = 1
            account_id = os.getenv("TMDB_ACCOUNT_ID").strip('""').strip("''")
            api_key = os.getenv("TMDB_API_KEY").strip('""').strip("''")
            session_id = os.getenv("TMDB_SESSION_ID").strip('""').strip("''")
            headers = {"accept": "application/json"}

            response = requests.get(
                f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US&session_id={session_id}, headers={headers}"
            )
            json_results = response.json()

            for genre in json_results["genres"]:
                MovieGenre.objects.update_or_create(
                    id=genre["id"],
                    name=genre["name"],
                )

            response = requests.get(
                f"https://api.themoviedb.org/3/account/{account_id}/rated/movies?api_key={api_key}&language=en-US&session_id={session_id}&sort_by=created_at.desc&page={page_number}, headers={headers}"
            )
            json_results = response.json()
            total_pages = json_results["total_pages"]
            poster_size = "w500"

            while page_number <= total_pages:
                response = requests.get(
                    f"https://api.themoviedb.org/3/account/{account_id}/rated/movies?api_key={api_key}&language=en-US&session_id={session_id}&sort_by=created_at.desc&page={page_number}"
                )
                json_results = response.json()

                for media in json_results["results"]:
                    # Check to see if Movie Page exists
                    if movie_exists(media["id"]):
                        # if it does exist, update the rating
                        MoviePage.objects.filter(movie_id=media["id"]).update(
                            rating=media["rating"]
                        )
                    else:
                        # if it does not exist, create a new Movie Page
                        self.save_media(media, movies_index_page, poster_size)

                        # Fetch movie credits first that has the person_id we want to fetch next
                        # See https://developer.themoviedb.org/reference/movie-credits
                        url = f"https://api.themoviedb.org/3/movie/{media['id']}/credits?api_key={api_key}&language=en-US&session_id={session_id}"
                        response = requests.get(url, headers=headers)
                        cast_results = response.json()

                        if cast_results["cast"]:
                            self.save_cast(cast_results)

                page_number += 1

            movies = MoviePage.objects.live().public().all()
            collection = Collection.objects.get(name="Movies")
            for movie in movies:
                if not movie.image:
                    self.get_poster(movie, collection)
