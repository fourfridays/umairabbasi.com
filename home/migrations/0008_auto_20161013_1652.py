# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 16:52
from __future__ import unicode_literals

import blog.models
from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20161012_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootstrap12',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock()), ('alignment', blog.models.ImageFormatChoiceBlock())), icon='image', label='Aligned image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('aligned_html', wagtail.wagtailcore.blocks.StructBlock((('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('alignment', blog.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')))),
        ),
    ]