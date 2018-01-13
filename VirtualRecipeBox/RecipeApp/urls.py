from django.conf.urls import url
from RecipeApp import views

urlpatterns = [
    url(r'^$',
        views.MyTemplateView.as_view(), name='home'),
    url(r'^recipes/$',
        views.RecipeListView.as_view(),
        name='recipe_list'),
    url(r'^favourites/(?P<pk>[0-9]+)/$',
        views.FavouritesListView.as_view(),
        name='favourites_list'),
]

