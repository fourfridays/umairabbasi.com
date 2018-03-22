# image_formats.py
from wagtail.images.formats import Format, register_image_format

register_image_format(Format('full-width', 'Full-Width', 'richtext-image full-width img-fluid img-thumbnail mx-auto d-block', 'width-1200'))