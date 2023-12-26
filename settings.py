from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = os.environ.get("DJANGO_DEBUG") == "True"

INSTALLED_APPS = [
    "anymail",
    "blog",
    "fontawesomefree",
    "page",
    "ratings",
    "taxonomy",
    "wagtailcodeblock",

    "wagtail.contrib.table_block",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.modeladmin",
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
        traces_sample_rate=0.2,
    )

ROOT_URLCONF = "urls"

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

WSGI_APPLICATION = "wsgi.application"

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite://:memory:")
DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/New_York"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = ["static"]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

staticfiles_backend = "django.contrib.staticfiles.storage.StaticFilesStorage"
STATIC_URL = "/static/"

if DEBUG is True:
    storage_backend = "django.core.files.storage.FileSystemStorage"
    MEDIA_URL = "media/"
    MEDIA_ROOT = os.path.join("/data/media")
else:
    AWS_S3_ACCESS_KEY_ID = os.environ.get("AWS_S3_ACCESS_KEY_ID", default=None)
    AWS_S3_SECRET_ACCESS_KEY = os.environ.get("AWS_S3_SECRET_ACCESS_KEY", default=None)
    AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", default=None)
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_FILE_OVERWRITE = os.environ.get("AWS_S3_FILE_OVERWRITE", default=False)
    AWS_QUERYSTRING_AUTH = os.environ.get("AWS_QUERYSTRING_AUTH", default=False)
    AWS_IS_GZIPPED = os.environ.get("AWS_IS_GZIPPED", default=True)
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000"
    }
    # S3 static settings
    # STATIC_LOCATION = "static"
    # STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"
    # staticfiles_backend = "page.storage_backends.StaticStorage"
    # S3 public media settings
    PUBLIC_MEDIA_LOCATION = "media"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"
    storage_backend = "page.storage_backends.PublicMediaStorage"
    # S3 private media settings
    PRIVATE_MEDIA_LOCATION = "private"
    PRIVATE_FILE_STORAGE = "page.storage_backends.PrivateMediaStorage"

STORAGES = {
    "default": {"BACKEND": storage_backend},
    "staticfiles": {"BACKEND": staticfiles_backend},
}

# Wagtail settings
WAGTAIL_SITE_NAME = os.environ.get(
    "WAGTAIL_SITE_NAME", default="Umair Abbasi"
)

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = os.environ.get("WAGTAILADMIN_BASE_URL", default="localhost")

DOMAIN_ALIASES = [
    d.strip() for d in os.environ.get("DOMAIN_ALIASES", "").split(",") if d.strip()
]
ALLOWED_HOSTS = DOMAIN_ALIASES
CSRF_TRUSTED_ORIGINS = [
    os.environ.get("CSRF_TRUSTED_ORIGINS", default="http://localhost")
]
SECRET_KEY = os.environ.get("SECRET_KEY", default="<a string of random characters>")

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
PREPEND_WWW = os.getenv("PREPEND_WWW", default=False)
SITE_ID = 1

# Make low-quality but small images
WAGTAILIMAGES_JPEG_QUALITY = 70
WAGTAILIMAGES_WEBP_QUALITY = 75
WAGTAIL_ENABLE_WHATS_NEW_BANNER = False
WAGTAILEMBEDS_FINDERS = [{"class": "wagtail.embeds.finders.oembed"}]

# wagtailcodeblock
WAGTAIL_CODE_BLOCK_LINE_NUMBERS = False
WAGTAIL_CODE_BLOCK_THEME = "tomorrow"
