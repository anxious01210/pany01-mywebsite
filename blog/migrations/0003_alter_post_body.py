# Generated by Django 4.2.8 on 2024-01-05 10:42

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_post_image_1"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="body",
            field=tinymce.models.HTMLField(),
        ),
    ]
