# Generated by Django 4.2.1 on 2023-07-08 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0013_cast_moviepage_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='ratings.people'),
        ),
    ]
