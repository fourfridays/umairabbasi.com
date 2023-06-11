from io import BytesIO

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.core.files.images import ImageFile

from wagtail.models import Page, Collection
from wagtail.images.models import Image
from ratings.models import MoviePage, TvPage
from datetime import datetime

import datetime, os, pathlib, requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        # ==============================
        # =           MOVIES           =
        # ==============================
        print("Pulling Movies")

        account_id = os.getenv("TMDB_ACCOUNT_ID").strip('""').strip("''")
        api_key = os.getenv("TMDB_API_KEY").strip('""').strip("''")
        session_id = os.getenv("TMDB_SESSION_ID").strip('""').strip("''")
        r = requests.get(
            "https://api.themoviedb.org/3/account/%s/rated/movies?api_key=%s&language=en-US&session_id=%s&sort_by=created_at.desc&page=1"
            % (account_id, api_key, session_id)
        )
        json_content = r.json()
        pages = json_content["total_pages"]
        parent_page = Page.objects.get(title="Movies").specific
        poster_size = "w500"

        for movie in json_content["results"]:
            try:
                movie_page = MoviePage(
                    tmdb_id=movie["id"],
                    title=movie["title"],
                    description=movie["overview"],
                    release_date=datetime.datetime.strptime(
                        movie["release_date"], "%Y-%m-%d"
                    ).date(),
                    rating=movie["rating"],
                    poster="https://image.tmdb.org/t/p/"
                    + poster_size
                    + movie["poster_path"],
                    language=movie["original_language"],
                )
                parent_page.add_child(instance=movie_page)
                movie_page.save()
            except ValidationError:
                m = MoviePage.objects.get(tmdb_id=movie["id"])
                # if we updated our movie rating for an existing movie in Wagtail
                if m.rating != movie["rating"]:
                    m.rating = movie["rating"]
                    m.save_revision().publish()
                else:
                    pass
                # if we updated poster size for an existing poster path in Wagtail
                m.poster = (
                    "https://image.tmdb.org/t/p/" + poster_size + movie["poster_path"]
                )
                m.save()

        page = 2

        while page <= pages:
            r = requests.get(
                "https://api.themoviedb.org/3/account/%s/rated/movies?api_key=%s&language=en-US&session_id=%s&sort_by=created_at.desc&page=%s"
                % (account_id, api_key, session_id, page)
            )
            json_content = r.json()

            for movie in json_content["results"]:
                try:
                    movie_page = MoviePage(
                        tmdb_id=movie["id"],
                        title=movie["title"],
                        description=movie["overview"],
                        release_date=datetime.datetime.strptime(
                            movie["release_date"], "%Y-%m-%d"
                        ).date(),
                        rating=movie["rating"],
                        poster="https://image.tmdb.org/t/p/"
                        + poster_size
                        + movie["poster_path"],
                        language=movie["original_language"],
                    )
                    parent_page.add_child(instance=movie_page)
                    movie_page.save()
                except ValidationError:
                    m = MoviePage.objects.get(tmdb_id=movie["id"])
                    if m.rating != movie["rating"]:
                        m.rating = movie["rating"]
                        m.save_revision().publish()
                    else:
                        pass

                    m.poster = (
                        "https://image.tmdb.org/t/p/"
                        + poster_size
                        + movie["poster_path"]
                    )
                    m.save()

            page = page + 1

        # ==========================
        # =           TV           =
        # ==========================
        print("Pulling TV Shows")

        r = requests.get(
            "https://api.themoviedb.org/3/account/%s/rated/tv?api_key=%s&language=en-US&session_id=%s&sort_by=created_at.desc&page=1"
            % (account_id, api_key, session_id)
        )
        json_content = r.json()
        pages = json_content["total_pages"]
        parent_page = Page.objects.get(title="TV").specific

        for tv in json_content["results"]:
            try:
                tv_page = TvPage(
                    tmdb_id=tv["id"],
                    title=tv["name"],
                    description=tv["overview"],
                    release_date=datetime.datetime.strptime(
                        tv["first_air_date"], "%Y-%m-%d"
                    ).date(),
                    rating=tv["rating"],
                    poster="https://image.tmdb.org/t/p/"
                    + poster_size
                    + tv["poster_path"],
                    language=tv["original_language"],
                )
                parent_page.add_child(instance=tv_page)
                tv_page.save()
            except ValidationError:
                t = TvPage.objects.get(tmdb_id=tv["id"])
                if t.rating != tv["rating"]:
                    t.rating = tv["rating"]
                    t.save_revision().publish()
                else:
                    pass

                t.poster = (
                    "https://image.tmdb.org/t/p/" + poster_size + tv["poster_path"]
                )
                t.save()

        page = 2

        while page <= pages:
            r = requests.get(
                "https://api.themoviedb.org/3/account/%s/rated/tv?api_key=%s&language=en-US&session_id=%s&sort_by=created_at.desc&page=%s"
                % (account_id, api_key, session_id, page)
            )
            json_content = r.json()

            for tv in json_content["results"]:
                try:
                    tv_page = TvPage(
                        tmdb_id=tv["id"],
                        title=tv["name"],
                        description=tv["overview"],
                        release_date=datetime.datetime.strptime(
                            tv["first_air_date"], "%Y-%m-%d"
                        ).date(),
                        rating=tv["rating"],
                        poster="https://image.tmdb.org/t/p/"
                        + poster_size
                        + tv["poster_path"],
                        language=tv["original_language"],
                    )
                    parent_page.add_child(instance=tv_page)
                    tv_page.save()
                except ValidationError:
                    t = TvPage.objects.get(tmdb_id=tv["id"])
                    if t.rating != tv["rating"]:
                        t.rating = tv["rating"]
                        t.save_revision().publish()
                    else:
                        pass

                    t.poster = (
                        "https://image.tmdb.org/t/p/" + poster_size + tv["poster_path"]
                    )
                    t.save()

            page = page + 1

        # ==========================================
        # =           PULLING  POSTERS             =
        # ==========================================
        def get_poster(media):
            response = requests.get(media.poster)
            filename = pathlib.Path(media.poster).name

            i = Image(
                title=media.title,
                file=ImageFile(BytesIO(response.content), name=filename),
                collection_id=collection.id,
            )
            i.save()
            i.tags.add("poster")
            media.image = i
            media.save()

        print("Pulling Movie Posters")
        movies = MoviePage.objects.all()
        collection = Collection.objects.get(name="Movies")
        for movie in movies:
            if not movie.image:
                get_poster(movie)

        print("Pulling TV Show Posters")
        tv_shows = TvPage.objects.all()
        collection = Collection.objects.get(name="TV")
        for tv in tv_shows:
            if not tv.image:
                get_poster(tv)
