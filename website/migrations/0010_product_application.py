# Generated by Django 3.2 on 2022-10-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='application',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
