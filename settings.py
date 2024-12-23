from pathlib import Path
import os
import dj_database_url
from django_storage_url import dsn_configured_storage_class

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    "anymail",
    "blog",
    "fontawesomefree",
    "microblog",
    "page",
    "ratings",
    "taxonomy",
    "wagtailcodeblock",
    "wagtail.contrib.table_block",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.routable_page",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.legacy.sitemiddleware.SiteMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

sentry_dsn = os.environ.get("SENTRY_DSN", "")
if sentry_dsn:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    def ignore_disallowedhost(event, hint):
        if event.get("logger", None) == "django.security.DisallowedHost":
            return None
        return event

    sentry_sdk.init(
        dsn=sentry_dsn,
        before_send=ignore_disallowedhost,
        integrations=[DjangoIntegration()],
        release=os.environ.get("GIT_COMMIT", "develop"),
        environment=os.environ.get("STAGE", "local"),
        traces_sample_rate=0.2,
    )

ROOT_URLCONF = "urls"

SECRET_KEY = os.environ.get("SECRET_KEY", "<a string of random characters>")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG") == "True"

DIVIO_DOMAIN = os.environ.get("DOMAIN", "")
DIVIO_DOMAIN_ALIASES = [
    d.strip() for d in os.environ.get("DOMAIN_ALIASES", "").split(",") if d.strip()
]
DIVIO_DOMAIN_REDIRECTS = [
    d.strip() for d in os.environ.get("DOMAIN_REDIRECTS", "").split(",") if d.strip()
]

ALLOWED_HOSTS = [DIVIO_DOMAIN] + DIVIO_DOMAIN_ALIASES + DIVIO_DOMAIN_REDIRECTS

CSRF_TRUSTED_ORIGINS = [
    os.environ.get("CSRF_TRUSTED_ORIGINS", default="https://umairabbasi.com")
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Authentication Backends
AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

# Search Backends
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

WSGI_APPLICATION = "wsgi.application"

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite://:memory:")

DATABASES = {
    "default": dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=0,
        conn_health_checks=False,
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
USE_I18N = True
USE_TZ = True
TIME_ZONE = "UTC"

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = ["static"]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files
# DEFAULT_FILE_STORAGE is configured using DEFAULT_STORAGE_DSN

# read the setting value from the environment variable
DEFAULT_STORAGE_DSN = os.environ.get("DEFAULT_STORAGE_DSN")

# dsn_configured_storage_class() requires the name of the setting
DefaultStorageClass = dsn_configured_storage_class("DEFAULT_STORAGE_DSN")

# Django's DEFAULT_FILE_STORAGE requires the class name
DEFAULT_FILE_STORAGE = "settings.DefaultStorageClass"

# only required for local file storage and serving, in development
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join("/data/media/")

WAGTAIL_SITE_NAME = "Umair Abbasi"
WAGTAILADMIN_BASE_URL = "https://umairabbasi.com/"

FLICKR_API_KEY = os.getenv("FLICKR_API_KEY", default="")
FLICKR_API_SECRET = os.getenv("FLICKR_API_SECRET", default="")
FLICKR_API_USER = os.getenv("FLICKR_API_USER", default="")

# DJANGO ANYMAIL
ANYMAIL = {
    "MAILGUN_API_KEY": os.getenv("MAILGUN_API_KEY", default=""),
    "MAILGUN_SENDER_DOMAIN": os.getenv("MAILGUN_SENDER_DOMAIN", default=""),
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", default="")
SERVER_EMAIL = os.getenv("SERVER_EMAIL", default="")

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
PREPEND_WWW = os.environ.get("PREPEND_WWW", default=False)
SITE_ID = 1

# Make low-quality but small images
WAGTAILIMAGES_JPEG_QUALITY = 70
WAGTAILIMAGES_WEBP_QUALITY = 75
WAGTAIL_ENABLE_WHATS_NEW_BANNER = False
WAGTAILEMBEDS_FINDERS = [{"class": "wagtail.embeds.finders.oembed"}]

# wagtailcodeblock
WAGTAIL_CODE_BLOCK_LINE_NUMBERS = False
WAGTAIL_CODE_BLOCK_THEME = "tomorrow"

# Logging configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "info.log"),
            "formatter": "verbose",
        },
        "sentry": {
            "level": "ERROR",  # Capture errors and above to Sentry
            "class": "sentry_sdk.integrations.logging.EventHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file", "sentry"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
