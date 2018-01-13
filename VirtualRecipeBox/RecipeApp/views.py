# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, DeleteView)
from RecipeApp.models import Recipe, Favourite
from django.core.urlresolvers import reverse
# Create your views here.

#from .forms import AddRecipeForm
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


#class RecipeCreateView(LoginRequiredMixin, CreateView):
    #template_name = 'addrecipe.html'
    #form_class = AddRecipeForm
    #model = Recipe

class CategoryListView(ListView):
    template_name = 'category.html'
    model = Recipe

    def get_queryset(self):
        return Recipe.objects.filter(category=self.kwargs['category'])

class MyRecipesListView(ListView):
    template_name = 'myrecipes.html'
    model = Recipe
    context_object_name = 'myrecipes'

class RecipeDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Recipe

    def get_success_url(self, *args, **kwargs):
        return reverse(
            'my_recipe_list',
            kwargs = {'pk': self.object.pk}
         )
