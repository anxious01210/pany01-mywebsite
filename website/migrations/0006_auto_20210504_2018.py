# Generated by Django 3.2 on 2021-05-04 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20210429_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(help_text='The type of categories used in this project.', max_length=100, to='website.Category'),
        ),
    ]
