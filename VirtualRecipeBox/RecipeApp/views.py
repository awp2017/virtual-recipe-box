# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,)
from RecipeApp.models import Recipe, Favourite
# Create your views here.


class MyTemplateView(TemplateView):
    template_name = 'index.html'


class RecipeListView(ListView):
    template_name = 'home.html';
    model = Recipe;
    context_object_name = 'recipes'

class FavouritesListView(ListView):
    template_name = 'favourites.html'
    model = Favourite
    context_object_name = 'favourites'



