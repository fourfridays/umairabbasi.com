from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from ratings.models import Cast, MovieGenre, People


class MovieGenreModelAdmin(ModelAdmin):
    model = MovieGenre
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_per_page = 50
    list_display = ('id', 'name')
    ordering = ['name']
    #list_filter = ('offering_id', 'offering_code')
    search_fields = ('name')


class PeopleModelAdmin(ModelAdmin):
    model = People
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_per_page = 50
    list_display = ('id', 'name')
    ordering = ['id', 'name']
    #list_filter = ('offering_id', 'offering_code')
    search_fields = ('id', 'name')


class CastModelAdmin(ModelAdmin):
    model = Cast
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_per_page = 50
    list_display = ('movie', 'cast_member', 'character')
    ordering = ['movie']
    #list_filter = ('offering_id', 'offering_code')
    search_fields = ('character')


# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(MovieGenreModelAdmin)
modeladmin_register(PeopleModelAdmin)
modeladmin_register(CastModelAdmin)
