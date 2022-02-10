# Generated by Django 4.0.2 on 2022-02-10 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpagetag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='taggit.tag'),
        ),
    ]
