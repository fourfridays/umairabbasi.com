# Architecture
This is my personal website viewable at https://umairabbasi.com. The website is built using [Wagtail](https://wagtail.org/) and hosted on [Divio](https://www.divio.com/). [Elasticsearch](https://www.elastic.co/) via [Bonsai](https://bonsai.io/) is used for search.

# Ratings App
The idea behind naming it a ratings app is to keep it open to rating other products outside Movies and TV Shows.

## Movies & TV Show Ratings
This app pulls all rated movies and TV shows on your TMDB account.

There are many robust tools available on GitHub for TMDB. This is a very simple implementation of retrieving all rated movies and tv shows. You may easily set this up for your own Wagtail website.

### API
The app is built using the free version of [The Movie Database API](https://developers.themoviedb.org/3/getting-started/introduction).

The API pulls all information and media and stores it locally in Wagtail.

### Setup
Create app ratings and copy over the code for models, views, and management/commands/pull_all_media_api.py.

Set environment variables "TMDB_ACCOUNT_ID", "TMDB_API_KEY", and "TMDB_SESSION_ID" for your account.

For the search interface you would need to set environment variable "ELASTIC_SEARCH_URL" for your elasticsearch implementation.

### Running the API
From the root folder of your project run:
` ./manage.py pull_all_media_api `

### To Do
- ability to add multiple watch dates (maybe)

# Contact
Feel free to reach me on [Twitter](https://twitter.com/fourfridays) or [Reddit](https://www.reddit.com/user/fourfridays/).
