# Generated by Django 3.0.11 on 2020-12-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20201221_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieviewdate',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
