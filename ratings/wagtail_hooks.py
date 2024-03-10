from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from ratings.models import Cast, MovieGenre, People


class MovieGenreSnippetViewSet(SnippetViewSet):
    model = MovieGenre
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_per_page = 50
    list_display = ('id', 'name')
    ordering = ['name']
    search_fields = ('name')


class PeopleSnippetViewSet(SnippetViewSet):
    model = People
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_per_page = 50
    list_display = ('id', 'name')
    ordering = ['id', 'name']
    search_fields = ('id', 'name')


class CastSnippetViewSet(SnippetViewSet):
    model = Cast
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_per_page = 50
    list_display = ('movie', 'cast_member', 'character')
    ordering = ['movie']
    search_fields = ('character')

register_snippet(MovieGenreSnippetViewSet)
register_snippet(PeopleSnippetViewSet)
register_snippet(CastSnippetViewSet)
