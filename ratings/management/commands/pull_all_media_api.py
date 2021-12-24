from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

from wagtail.core.models import Page
from ratings.models import MoviePage, TvPage
from datetime import datetime

import requests
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        # ==============================
        # =           MOVIES           =
        # ==============================
        account_id = os.getenv('TMDB_ACCOUNT_ID').strip('""').strip('\'\'')
        api_key = os.getenv('TMDB_API_KEY').strip('""').strip('\'\'')
        session_id = os.getenv('TMDB_SESSION_ID').strip('""').strip('\'\'')
        r = requests.get('https://api.themoviedb.org/3/account/%s/rated/movies?api_key=%s&language=en-US&session_id=%s&sort_by=created_at.desc&page=1' % (account_id, api_key, session_id))
        json_content = r.json()
        pages = json_content['total_pages']
        parent_page = Page.objects.get(title='Movies').specific

        for movie in json_content['results']:
            try:
                movie_page = MoviePage(tmdb_id=movie['id'], title = movie['title'], description = movie['overview'], release_date = movie['release_date'], rating = movie['rating'], poster = 'https://image.tmdb.org/t/p/w300' + movie['poster_path'], language = movie['original_language'])
                parent_page.add_child(instance=movie_page)
                movie_page.save()
            except ValidationError:
                m = MoviePage.objects.get(tmdb_id = movie['id'])
                if m.rating != movie['rating']:
                    m.rating = movie['rating']
                    m.save_revision().publish()
                else:
                    pass

        page = 2

        while page <= pages:
            r = requests.get('https://api.themoviedb.org/3/account/%s/rated/movies?api_key=%s&language=en-US&session_id=%s&sort_by=created_at.desc&page=%s' % (account_id, api_key, session_id, page))
            json_content = r.json()

            for movie in json_content['results']:
                try:
                    movie_page = MoviePage(tmdb_id=movie['id'], title = movie['title'], description = movie['overview'], release_date = movie['release_date'], rating = movie['rating'], poster = 'https://image.tmdb.org/t/p/w300' + movie['poster_path'], language = movie['original_language'])
                    parent_page.add_child(instance=movie_page)
                    movie_page.save()
                except ValidationError:
                    m = MoviePage.objects.get(tmdb_id = movie['id'])
                    if m.rating != movie['rating']:
                        m.rating = movie['rating']
                        m.save_revision().publish()
                    else:
                        pass

            page = page + 1

        # ==========================
        # =           TV           =
        # ==========================
        r = requests.get('https://api.themoviedb.org/3/account/%s/rated/tv?api_key=%s&language=en-US&session_id=%s&sort_by=created_at.desc&page=1' % (account_id, api_key, session_id))
        json_content = r.json()
        pages = json_content['total_pages']
        parent_page = Page.objects.get(title='TV').specific

        for tv in json_content['results']:
            try:
                tv_page = TvPage(tmdb_id=tv['id'], title = tv['name'], description = tv['overview'], release_date = tv['first_air_date'], rating = tv['rating'], poster = 'https://image.tmdb.org/t/p/w300' + tv['poster_path'], language = tv['original_language'])
                parent_page.add_child(instance=tv_page)
                tv_page.save()
            except ValidationError:
                t = TvPage.objects.get(tmdb_id = tv['id'])
                if t.rating != tv['rating']:
                    t.rating = tv['rating']
                    t.save_revision().publish()
                else:
                    pass

        page = 2

        while page <= pages:
            r = requests.get('https://api.themoviedb.org/3/account/%s/rated/tv?api_key=%s&language=en-US&session_id=%s&sort_by=created_at.desc&page=%s' % (account_id, api_key, session_id, page))
            json_content = r.json()

            for tv in json_content['results']:
                try:
                    tv_page = TvPage(tmdb_id=tv['id'], title = tv['name'], description = tv['overview'], release_date = tv['first_air_date'], rating = tv['rating'], poster = 'https://image.tmdb.org/t/p/w300' + tv['poster_path'], language = tv['original_language'])
                    parent_page.add_child(instance=tv_page)
                    tv_page.save()
                except ValidationError:
                    t = TvPage.objects.get(tmdb_id = tv['id'])
                    if t.rating != tv['rating']:
                        t.rating = tv['rating']
                        t.save_revision().publish()
                    else:
                        pass

            page = page + 1