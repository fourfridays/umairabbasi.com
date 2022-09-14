# Generated by Django 4.0.7 on 2022-09-13 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('ratings', '0005_moviepage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvpage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Testing image pull from poster URLField', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
