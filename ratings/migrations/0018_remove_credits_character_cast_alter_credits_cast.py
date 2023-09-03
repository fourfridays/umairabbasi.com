# Generated by Django 4.2.1 on 2023-07-09 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0017_remove_credits_people_credits_cast'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credits',
            name='character',
        ),
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.TextField(help_text='Max length 100 characters', max_length=100)),
                ('cast_member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ratings.people')),
            ],
        ),
        migrations.AlterField(
            model_name='credits',
            name='cast',
            field=models.ManyToManyField(to='ratings.cast'),
        ),
    ]