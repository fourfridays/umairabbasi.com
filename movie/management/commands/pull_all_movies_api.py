from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from movie.models import *
from datetime import datetime

import requests
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        account_id = os.getenv('account_id').strip('""').strip('\'\'')
        api_key = os.getenv('api_key').strip('""').strip('\'\'')
        session_id = os.getenv('session_id').strip('""').strip('\'\'')
        r = requests.get('https://api.themoviedb.org/3/account/%s/rated/movies?api_key=%s&language=en-US&session_id=%s&sort_by=created_at.desc&page=1' % (account_id, api_key, session_id))
        json_content = r.json()
        pages = json_content['total_pages']

        for movie in json_content['results']:
            try:
                Movie.objects.update_or_create(title = movie['title'], overview = movie['overview'], release_date = movie['release_date'], rating = movie['rating'], poster = 'https://image.tmdb.org/t/p/w300' + movie['poster_path'], language = movie['original_language'])
                m = Movie.objects.get(title = movie['title'])
                m.save()
            except:
                Movie.objects.filter(title = movie['title']).update(overview = movie['overview'], release_date = movie['release_date'], rating = movie['rating'], poster = 'https://image.tmdb.org/t/p/w300' + movie['poster_path'], language = movie['original_language'])
                m = Movie.objects.get(title = movie['title'])
                m.save()

        page = 2

        while page <= pages:
            r = requests.get('https://api.themoviedb.org/3/account/%s/rated/movies?api_key=%s&language=en-US&session_id=%s&sort_by=created_at.desc&page=%s' % (account_id, api_key, session_id, page))
            json_content = r.json()

            for movie in json_content['results']:
                try:
                    Movie.objects.update_or_create(title = movie['title'], overview = movie['overview'], release_date = movie['release_date'], rating = movie['rating'], poster = 'https://image.tmdb.org/t/p/w300' + movie['poster_path'], language = movie['original_language'])
                    m = Movie.objects.get(title = movie['title'])
                    m.save()
                except:
                    Movie.objects.filter(title = movie['title']).update(overview = movie['overview'], release_date = movie['release_date'], rating = movie['rating'], poster = 'https://image.tmdb.org/t/p/w300' + movie['poster_path'], language = movie['original_language'])
                    m = Movie.objects.get(title = movie['title'])
                    m.save()

            page = page + 1