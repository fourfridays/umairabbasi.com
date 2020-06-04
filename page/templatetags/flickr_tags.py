from django import template
from django.conf import settings
import flickrapi
import json

register = template.Library()


# Flickr Tag
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