# Generated by Django 4.2.7 on 2023-12-28 20:51

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='microblogpage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'bold', 'italic', 'link', 'code'], icon='pilcrow', template='blocks/paragraph_block.html'))], use_json_field=True),
        ),
    ]
