from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from blog.models import Comment


class CommentModelAdmin(ModelAdmin):
    model = Comment
    menu_icon = 'date'
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_per_page = 50
    list_display = ('user', 'active', 'article', 'content', 'created_on')
    ordering = ['created_on']
    #list_filter = ('offering_id', 'offering_code')
    search_fields = ('user', 'article', 'created_on')

modeladmin_register(CommentModelAdmin)