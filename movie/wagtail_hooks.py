from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from movie.models import *


class MovieModelAdmin(ModelAdmin):
    model = Movie
    menu_icon = 'date'  # change as required
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_per_page = 50
    list_display = ('title', 'view_date', 'release_date')
    ordering = ['title', 'view_date']
    #list_filter = ('offering_id', 'offering_code')
    search_fields = ('title', 'view_date')

modeladmin_register(MovieModelAdmin)