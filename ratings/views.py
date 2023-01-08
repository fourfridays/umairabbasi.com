from django.shortcuts import render

from ratings.models import *
from wagtail.search.models import Query


def movie_search(request):
    search_query = request.GET.get("query", None)
    if search_query:
        search_results = MoviePage.objects.live().search(search_query)
        movie_count = MoviesIndexPage.get_movie_count(request, search_results)
        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()

        return render(
            request,
            "ratings/movies_index_page.html",
            {
                "search_query": search_query,
                "movie_count": movie_count,
                "media": search_results,
            },
        )
    else:
        search_results = MoviePage.objects.live().order_by("title")

    # Render template
    return render(
        request,
        "ratings/movies_index_page.html",
        {
            "media": search_results,
        },
    )


def tv_search(request):
    search_query = request.GET.get("query", None)
    if search_query:
        search_results = TvPage.objects.live().search(search_query)
        tv_count = TvIndexPage.get_tv_count(request, search_results)
        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()

        return render(
            request,
            "ratings/tv_index_page.html",
            {
                "search_query": search_query,
                "tv_count": tv_count,
                "media": search_results,
            },
        )
    else:
        search_results = TvPage.objects.live().order_by("title")

    # Render template
    return render(
        request,
        "ratings/tv_index_page.html",
        {
            "media": search_results,
        },
    )
