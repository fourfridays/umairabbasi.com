# Generated by Django 3.0.13 on 2021-03-28 01:43

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingsIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='moviepage',
            name='watch_party',
            field=wagtail.core.fields.StreamField([('view_block', wagtail.core.blocks.StructBlock([('date', wagtail.core.blocks.DateBlock(required=False)), ('people', wagtail.core.blocks.StreamBlock([('person', wagtail.snippets.blocks.SnippetChooserBlock('page.People'))]))]))], blank=True, default=''),
        ),
    ]
