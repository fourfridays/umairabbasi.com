# Generated by Django 4.2.1 on 2023-07-09 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0014_alter_cast_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.TextField(help_text='Max length 100 characters', max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='moviepage',
            old_name='tmdb_id',
            new_name='movie_id',
        ),
        migrations.RenameField(
            model_name='tvpage',
            old_name='tmdb_id',
            new_name='tv_id',
        ),
        migrations.DeleteModel(
            name='Cast',
        ),
        migrations.AddField(
            model_name='credits',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ratings.moviepage'),
        ),
        migrations.AddField(
            model_name='credits',
            name='people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ratings.people'),
        ),
    ]
