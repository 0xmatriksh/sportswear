# Generated by Django 3.0.7 on 2020-06-10 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
    ]
