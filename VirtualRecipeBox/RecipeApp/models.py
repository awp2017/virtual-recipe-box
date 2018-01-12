# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=45)
    category = models.IntegerField(choices=[
        (1, "Soup"),
        (2, "Dessert"),
        (3, "Main Course"),
        (4, "Salad/ Starter"),
    ]
    )
    no_portions = models.IntegerField()
    text= models.TextField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id_user = models.ForeignKey(User)

class Favourite(models.Model):
    id_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=45)
    cantity = models.FloatField(null=False)
    unit = models.CharField(max_length=10)
    id_receip = models.ForeignKey(Recipe)

    def __str__(self):
        return self.name