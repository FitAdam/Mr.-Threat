"""Defines URL patterns for web_app."""

from django.urls import path

from . import views

app_name = 'web_app'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Search page
    path('search/', views.search, name='search'),
    # Page that shows threat intelligence
    path('the_results/', views.the_results, name='the_results'),
]
