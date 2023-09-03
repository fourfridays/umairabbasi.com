# Generated by Django 4.2.1 on 2023-07-08 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0012_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='ratings.people')),
                ('character', models.TextField(help_text='Max length 100 characters', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='moviepage',
            name='people',
            field=models.ManyToManyField(to='ratings.people'),
        ),
    ]