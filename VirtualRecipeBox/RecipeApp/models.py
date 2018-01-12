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
    text = models.TextField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id_user = models.ForeignKey(User)

    def __str__(self):
        return self.name


