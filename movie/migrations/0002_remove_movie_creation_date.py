# Generated by Django 2.2.9 on 2020-06-02 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='creation_date',
        ),
    ]
