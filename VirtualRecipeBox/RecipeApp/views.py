# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView)
from RecipeApp.models import Recipe, Favourite
# Create your views here.

from .forms import AddRecipeForm
from .models import Favourite, Recipe



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

    def get_queryset(self, *args, **kwargs):
        return Favourite.objects.all()


# class RecipeCreateView(CreateView):
#     template_name = 'addrecipe.html'
#     form_class = AddRecipeForm
#     model = Recipe

class MyRecipesView(ListView):
    template_name = 'myrecipes.html'
    model = Recipe
    context_object_name = 'myrecipes'

    def get_queryset(self, *args, **kwargs):
        return Recipe.objects.all()