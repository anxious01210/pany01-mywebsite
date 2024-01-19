# Generated by Django 4.2.8 on 2024-01-19 15:07

from django.db import migrations
import filebrowser.fields


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_post_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image_1",
            field=filebrowser.fields.FileBrowseField(
                blank=True, max_length=200, null=True, verbose_name="Image"
            ),
        ),
    ]
