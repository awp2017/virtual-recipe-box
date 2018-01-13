# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils import http
from django.utils.decorators import method_decorator
from django.views.generic import (TemplateView, ListView,CreateView, DetailView)
from RecipeApp.models import Recipe, Favourite
# Create your views here.

from .models import Favourite, Recipe
from .forms import AddRecipeForm

class MyTemplateView(TemplateView):
    template_name = 'index.html'


class RecipeListView(ListView):
    template_name = 'home.html'
    model = Recipe
    context_object_name = 'recipes'


class FavouritesListView(ListView):
    template_name = 'favourites.html'
    model = Favourite
    context_object_name = 'favourites'

    def get_queryset(self, *args, **kwargs):
        return Favourite.objects.all()


class RecipeCreateView(CreateView):
    template_name = 'addrecipe.html'
    form_class = AddRecipeForm
    model = Recipe

    def form_valid(self, form):
            form.instance.id_user = self.request.user
            return super(RecipeCreateView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse(
            'recipe_list',
            kwargs={'pk': self.object.pk}
        )
class RecipeDetailView(DetailView):
    template_name = 'details.html'
    model = Recipe
    context_object_name = 'recipes'