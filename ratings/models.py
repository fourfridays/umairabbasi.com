from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.search import index
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, re_path

from page.blocks import PersonDateBlock


class MovieGenre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=255, help_text="Max length 255 characters")

    def __str__(self):
        return f"{self.name}"


class TvGenre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=255, help_text="Max length 255 characters")

    def __str__(self):
        return f"{self.name}"


class People(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, help_text="Max Characters 100")
    image = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name}"


class MoviePage(Page):
    parent_page_types = ["MoviesIndexPage"]
    movie_id = models.IntegerField(unique=True, default=None)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.IntegerField(blank=True)
    poster = models.URLField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Testing image pull from poster URLField",
    )
    language = models.CharField(max_length=2, blank=True)
    genre = models.ManyToManyField(MovieGenre)
    watch_party = StreamField(
        [
            ("view_block", PersonDateBlock()),
        ],
        use_json_field=True,
        default="",
        blank=True,
    )

    search_fields = Page.search_fields + [  # Inherit search_fields from Page
        index.SearchField("title", partial_match=True),
        index.FilterField("rating", partial_match=True),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("movie_id"),
        FieldPanel("description"),
        FieldPanel("release_date"),
        FieldPanel("rating"),
        FieldPanel("poster"),
        FieldPanel("image"),
        FieldPanel("language"),
        FieldPanel("genre"),
        FieldPanel("watch_party"),
    ]

    def get_context(self, request):
        context = super(MoviePage, self).get_context(request)
        context["cast_members"] = Cast.objects.filter(movie=self).select_related(
            "cast_member"
        )
        return context


class Cast(models.Model):
    movie = models.ForeignKey(
        MoviePage,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    cast_member = models.ForeignKey(People, on_delete=models.PROTECT)
    character = models.TextField(
        max_length=100, help_text="Max length 100 characters"
    )

    def __str__(self):
        return f"{self.cast_member}"


class MoviesIndexPage(RoutablePageMixin, Page):
    subpage_types = ["MoviePage"]

    def get_movie_count(self, movies):
        movie_count = movies.count()
        return movie_count

    def get_context(self, request):
        context = super(MoviesIndexPage, self).get_context(request)
        context["title"] = "Movie Ratings"
        context["media"] = MoviePage.objects.live().order_by("-release_date")
        context["movie_count"] = self.get_movie_count(context["media"])
        return context

    @re_path(r"^top-rated/$")
    def top_recommended(self, request):
        """
        View function for must-watch movies
        """
        filtered_results = MoviePage.objects.filter(rating__gte=7).order_by(
            "-release_date"
        )
        movie_count = self.get_movie_count(filtered_results)

        return self.render(
            request,
            context_overrides={
                "title": "Movies Rated: Top-Rated",
                "rating": "top-rated",
                "media": filtered_results,
                "movie_count": movie_count,
            },
        )

    @re_path(r"^recommended/$")
    def recommended(self, request):
        """
        View function for must-watch movies
        """
        filtered_results = (
            MoviePage.objects.filter(rating__gte=4)
            .filter(rating__lte=6)
            .order_by("-release_date")
        )
        movie_count = self.get_movie_count(filtered_results)

        return self.render(
            request,
            context_overrides={
                "title": "Movies Rated: Recommended",
                "rating": "recommended",
                "media": filtered_results,
                "movie_count": movie_count,
            },
        )

    @re_path(r"^not-recommended/$")
    def not_recommended(self, request):
        """
        View function for must-watch movies
        """
        filtered_results = MoviePage.objects.filter(rating__lte=3).order_by(
            "-release_date"
        )
        movie_count = self.get_movie_count(filtered_results)

        return self.render(
            request,
            context_overrides={
                "title": "Movies Rated: Not-Recommended",
                "rating": "not-recommended",
                "media": filtered_results,
                "movie_count": movie_count,
            },
        )


class TvPage(Page):
    parent_page_types = ["TvIndexPage"]
    tv_id = models.IntegerField(unique=True, default=None)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.IntegerField(blank=True)
    poster = models.URLField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Testing image pull from poster URLField",
    )
    language = models.CharField(max_length=2, blank=True)
    genre = models.ManyToManyField(TvGenre)
    watch_party = StreamField(
        [
            ("view_block", PersonDateBlock()),
        ],
        use_json_field=True,
        default="",
        blank=True,
    )

    search_fields = Page.search_fields + [  # Inherit search_fields from Page
        index.SearchField("title", partial_match=True),
        index.FilterField("rating", partial_match=True),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("tv_id"),
        FieldPanel("description"),
        FieldPanel("release_date"),
        FieldPanel("rating"),
        FieldPanel("poster"),
        FieldPanel("image"),
        FieldPanel("language"),
        FieldPanel("genre"),
        FieldPanel("watch_party"),
    ]

    def get_context(self, request):
        context = super(TvPage, self).get_context(request)
        context["cast_members"] = TvCast.objects.filter(tv=self).select_related(
            "cast_member"
        )
        return context


class TvCast(models.Model):
    tv = models.ForeignKey(
        TvPage,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    cast_member = models.ForeignKey(People, on_delete=models.PROTECT)
    character = models.TextField(
        max_length=100, help_text="Max length 100 characters"
    )

    def __str__(self):
        return f"{self.cast_member}"


class TvIndexPage(RoutablePageMixin, Page):
    subpage_types = ["TvPage"]

    def get_tv_count(self, tv):
        tv_count = tv.count()
        return tv_count

    def get_context(self, request):
        context = super(TvIndexPage, self).get_context(request)
        context["title"] = "TV Show Ratings"
        context["media"] = (
            TvPage.objects.live().filter(rating__gte=7).order_by("-release_date")
        )
        context["tv_count"] = context["media"].count()
        return context

    @re_path(r"^top-rated/$")
    def top_recommended(self, request):
        """
        View function for must-watch movies
        """
        filtered_results = TvPage.objects.filter(rating__gte=7).order_by(
            "-release_date"
        )
        tv_count = self.get_tv_count(filtered_results)

        return self.render(
            request,
            context_overrides={
                "title": "TV Shows Rated: Top-Rated",
                "rating": "top-rated",
                "media": filtered_results,
                "tv_count": tv_count,
            },
        )

    @re_path(r"^recommended/$")
    def recommended(self, request):
        """
        View function for must-watch movies
        """
        filtered_results = (
            TvPage.objects.filter(rating__gte=4)
            .filter(rating__lte=6)
            .order_by("-release_date")
        )
        tv_count = self.get_tv_count(filtered_results)

        return self.render(
            request,
            context_overrides={
                "title": "TV Shows Rated: Recommended",
                "rating": "recommended",
                "media": filtered_results,
                "tv_count": tv_count,
            },
        )

    @re_path(r"^not-recommended/$")
    def not_recommended(self, request):
        """
        View function for must-watch movies
        """
        filtered_results = TvPage.objects.filter(rating__lte=3).order_by(
            "-release_date"
        )
        tv_count = self.get_tv_count(filtered_results)

        return self.render(
            request,
            context_overrides={
                "title": "TV Shows Rated: Not-Recommended",
                "rating": "not-recommended",
                "media": filtered_results,
                "tv_count": tv_count,
            },
        )


class RatingsIndexPage(Page):
    def get_context(self, request):
        context = super(RatingsIndexPage, self).get_context(request)
        context["movie_page"] = MoviePage.objects.get(title="Layer Cake")
        context["tv_page"] = TvPage.objects.get(title="Foundation")
        return context
