# Generated by Django 4.0.4 on 2022-05-18 22:08

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_tvindexpage_tvpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviepage',
            name='watch_party',
            field=wagtail.fields.StreamField([('view_block', wagtail.blocks.StructBlock([('date', wagtail.blocks.DateBlock(required=False)), ('people', wagtail.blocks.StreamBlock([('person', wagtail.snippets.blocks.SnippetChooserBlock('page.People'))]))]))], blank=True, default='', use_json_field=True),
        ),
        migrations.AlterField(
            model_name='tvpage',
            name='watch_party',
            field=wagtail.fields.StreamField([('view_block', wagtail.blocks.StructBlock([('date', wagtail.blocks.DateBlock(required=False)), ('people', wagtail.blocks.StreamBlock([('person', wagtail.snippets.blocks.SnippetChooserBlock('page.People'))]))]))], blank=True, default='', use_json_field=True),
        ),
    ]
