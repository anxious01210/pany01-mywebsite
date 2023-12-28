# Generated by Django 3.2 on 2021-04-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_product_product_manual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='packaging',
            field=models.CharField(blank=True, default=' KG', help_text='Enter the package weight.', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_manual',
            field=models.FileField(blank=True, null=True, upload_to='manuals/products'),
        ),
    ]
