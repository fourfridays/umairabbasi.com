# Generated by Django 3.0.6 on 2020-06-03 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(unique=True)),
                ('slug', models.SlugField(blank=True, max_length=120, null=True, unique=True)),
                ('overview', models.TextField()),
                ('release_date', models.CharField(blank=True, max_length=10)),
                ('rating', models.IntegerField(blank=True)),
                ('poster', models.URLField(blank=True)),
                ('language', models.CharField(blank=True, max_length=2)),
                ('creation_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
