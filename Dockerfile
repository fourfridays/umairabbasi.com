FROM python:3.11.7-slim-bookworm

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libmagic1 \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    git \
 && rm -rf /var/lib/apt/lists/*

# set the working directory
WORKDIR /app
# copy the repository files to it
COPY . /app

COPY requirements.* /app/

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput --clear

EXPOSE 80

# GUNICORN
CMD ["gunicorn", "--bind", ":80", "--workers", "1", "--threads", "2", "--worker-class", "gevent", "--max-requests-jitter", " 2000", "--max-requests", "1500", "wsgi"]