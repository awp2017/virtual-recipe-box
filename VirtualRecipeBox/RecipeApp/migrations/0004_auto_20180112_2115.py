# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-12 21:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeApp', '0003_remove_recipe_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='id_recipe',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='id_user',
        ),
        migrations.DeleteModel(
            name='Favourite',
        ),
    ]
