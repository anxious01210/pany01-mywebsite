# Generated by Django 3.2 on 2022-10-28 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20221028_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(help_text='Do not enter any data here. This is an autopopulate field from "Product Name" field.', unique=True),
        ),
    ]