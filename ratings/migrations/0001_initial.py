# Generated by Django 3.0.13 on 2021-03-28 00:59

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoviePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', models.TextField()),
                ('release_date', models.CharField(blank=True, max_length=10)),
                ('rating', models.IntegerField(blank=True)),
                ('poster', models.URLField(blank=True)),
                ('language', models.CharField(blank=True, max_length=2)),
                ('tmdb_id', models.IntegerField(default=None, unique=True)),
                ('watch_party', wagtail.fields.StreamField([('view_block', wagtail.blocks.StructBlock([('date', wagtail.blocks.DateBlock(required=False)), ('people', wagtail.blocks.StreamBlock([('person', wagtail.snippets.blocks.SnippetChooserBlock('page.People'))]))]))], default='')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MoviesIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
