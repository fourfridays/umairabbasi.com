# Generated by Django 3.0.6 on 2020-06-03 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='creation_date',
        ),
    ]
