# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-13 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeApp', '0002_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default=b'media/no-img-jpg', upload_to=b'media/'),
        ),
    ]