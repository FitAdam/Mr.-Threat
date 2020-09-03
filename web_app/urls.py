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
    # Page that shows user's searched IPs
    path('searched_ips/', views.searched_ips, name='searched_ips'),
    # Page that shows user's saved IP
    path('the_searched_ip/<int:ip_id>/', views.the_searched_ip, name='the_searched_ip'),
]
