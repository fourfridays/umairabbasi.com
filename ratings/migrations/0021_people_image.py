# Generated by Django 4.2.1 on 2023-07-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0020_cast_movie_delete_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
