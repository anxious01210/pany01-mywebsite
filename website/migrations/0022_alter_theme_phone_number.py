# Generated by Django 3.2 on 2022-12-29 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_theme_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='phone_number',
            field=models.CharField(blank=True, help_text='This is the Phone Number showed on each Topbar & Footer of the whole website. example ==> (+964) 750 450 6664', max_length=21),
        ),
    ]