# Generated by Django 2.2.7 on 2019-12-24 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpeoplerelationship_people'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogindexpage',
            old_name='image',
            new_name='hero_image',
        ),
        migrations.RenameField(
            model_name='blogpage',
            old_name='image',
            new_name='hero_image',
        ),
    ]
