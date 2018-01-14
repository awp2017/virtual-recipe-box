# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, DeleteView)
from RecipeApp.models import Recipe, Favourite
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
# Create your views here.

#from .forms import AddRecipeForm
from .models import Favourite, Recipe
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, AddRecipeForm



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
            kwargs={'pk': self.object.pk}
         )


class RecipeCreateView(CreateView):
    template_name = 'addrecipe.html'
    form_class = AddRecipeForm
    model = Recipe

    def form_valid(self, form):
        form.instance.id_user = self.request.user
        return super(RecipeCreateView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse(
            'my_recipe_list',
            kwargs={'pk': self.object.pk}
        )


def login_view(request):
    context = {}
    if request.method == 'GET':
        form = LoginForm()
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request=request,
                      user=user)
                return redirect('recipe_list')
            else:
                context['error_message'] = 'Wrong username or password!'
    context['form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')


class RecipeDetailView(DetailView):
    template_name = 'details.html'
    model = Recipe
    context_object_name = 'recipe'