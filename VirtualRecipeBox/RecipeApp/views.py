# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, TemplateView
# Create your views here.
import RecipeApp.models


class MyTemplateView(TemplateView):
    template_name = 'index.html'


class RecipeListView(ListView):
    template_name = 'home.html'
    model = RecipeApp.models.Recipe
    context_object_name = 'recipes'




