from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from wagtail.core.models import Page
from ratings.models import MoviePage
from datetime import datetime

import requests
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
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
            except:
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
                except:
                    pass

            page = page + 1