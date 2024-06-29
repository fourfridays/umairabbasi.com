import datetime, os, pathlib, requests, time

from settings import DEBUG

from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.files.images import ImageFile

from wagtail.models import Collection
from wagtail.images.models import Image

from algoliasearch.search_client import SearchClient
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

    def movie_exists(self, movie_id):
        try:
            MoviePage.objects.get(movie_id=movie_id)
            return True
        except ObjectDoesNotExist:
            return False

    def index_movies(self, movie):
        algolia_app_id = os.environ.get("ALGOLIA_APP_ID", "")
        algolia_api = os.environ.get("ALGOLIA_API", "")
        client = SearchClient.create(algolia_app_id, algolia_api)
        index = client.init_index("movie_index")

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

    def handle(self, *args, **options):
        # Check to see if MovieIndexPage exists
        movies_index_page = MoviesIndexPage.objects.live().public().get()

        # Get movies rated by user if movies_index_page exists
        if movies_index_page:
            page_number = 1
            account_id = os.getenv("TMDB_ACCOUNT_ID").strip('""').strip("''")
            api_key = os.getenv("TMDB_API_KEY").strip('""').strip("''")
            session_id = os.getenv("TMDB_SESSION_ID").strip('""').strip("''")
            headers = {"accept": "application/json"}

            # Movie Genres
            response = requests.get(
                f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US&session_id={session_id}, headers={headers}"
            )
            json_results = response.json()

            for genre in json_results["genres"]:
                MovieGenre.objects.update_or_create(
                    id=genre["id"],
                    name=genre["name"],
                )

            # Rated Movies
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
                    if self.movie_exists(media["id"]):
                        # if exists, update the rating
                        MoviePage.objects.filter(movie_id=media["id"]).update(
                            rating=media["rating"]
                        )
                    else:
                        # if it does not exist, create a new Movie Page
                        self.save_media(media, movies_index_page, poster_size)

                        # Fetch movie credits has the person_id we would need to save in People
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
                # If no poster, get poster
                if not movie.image:
                    self.get_poster(movie, collection)
                
                # Index the movie if not debug
                if not DEBUG:
                    self.index_movies(movie)
