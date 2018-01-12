# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views.generic import (
    View,
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView,
)

# Create your views here.
from .forms import AddRecipeForm
from .models import Favourite, Recipe


class FavRecipeListView(ListView):
    template_name = 'favourites.html'
    model = Favourite
    context_object_name = 'Favourites recipes'

    def get_queryset(self, *args, **kwargs):
        return Favourite.objects.all()


class RecipeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'addrecipe.html'
    form_class = AddRecipeForm
    model = Recipe