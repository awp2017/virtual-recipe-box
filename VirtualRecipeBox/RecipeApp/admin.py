# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from RecipeApp.models import Recipe, Favourite

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Favourite)