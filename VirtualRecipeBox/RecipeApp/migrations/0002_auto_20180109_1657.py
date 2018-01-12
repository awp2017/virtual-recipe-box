# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-09 16:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RecipeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RecipeApp.Recipe')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='followers',
            field=models.ManyToManyField(related_name='users_following', through='RecipeApp.Favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]