from django.conf import settings
from django.urls import path, include, re_path
from django.contrib import admin
from django.views.generic import TemplateView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap

from ratings.views import MovieIndexView, CastView, TvIndexView


urlpatterns = [
    path("django-admin/", admin.site.urls),
    re_path(
        r"^robots\.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain"
        ),
    ),
    path("ratings/movies/", MovieIndexView.as_view(), name="movie-index"),
    path(
        "ratings/cast/<int:people_id>/",
        CastView.as_view(),
        name="cast",
    ),
    path("ratings/tv/", TvIndexView.as_view(), name="tv-index"),
    path("__debug__/", include("debug_toolbar.urls")),
    re_path(r"^sitemap\.xml$", sitemap),
    re_path(r"^admin/", include(wagtailadmin_urls)),
    re_path(r"^documents/", include(wagtaildocs_urls)),
    re_path(r"", include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
