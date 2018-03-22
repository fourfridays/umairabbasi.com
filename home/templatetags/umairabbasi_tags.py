from datetime import date
from django import template
from django.conf import settings
import flickrapi
import json

from wagtail.core.models import Page

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()

def has_children(page):
    # Generically allow index pages to list their children
    return page.get_children().live().exists()

def is_active(page, current_page):
    # To give us active state on main navigation
    return (current_page.url.startswith(page.url) if current_page else False)


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('demo/tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

# Flickr Tag
# settings value
@register.simple_tag
def get_flickr_api_key():
    return getattr(settings, 'FLICKR_API_KEY', "")

@register.simple_tag
def get_flickr_api_secret():
    return getattr(settings, 'FLICKR_API_SECRET', "")

@register.simple_tag
def get_flickr_api_user():
    return getattr(settings, 'FLICKR_API_USER', "")

@register.inclusion_tag('tags/flickr_api.html', takes_context=True)
def flickr_photosets(context, photoset_id):
    flickr = flickrapi.FlickrAPI(get_flickr_api_key(), get_flickr_api_secret(), format='json')
    raw_flickr_json = flickr.photosets.getPhotos(photoset_id=photoset_id, user_id=get_flickr_api_user())
    parsed_flickr_json = json.loads(raw_flickr_json.decode('utf-8'))
    return {
        'flickr_json': parsed_flickr_json,
        'request': context['request'],
    }