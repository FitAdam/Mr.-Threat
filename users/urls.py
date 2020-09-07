"""Defines URL patterns for users."""

from django.urls import path, include
from . import views
app_name = 'users'

urlpatterns = [
    # Include default auth urls.
    path("", include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
    # Account view page.
    path('account_view/', views.account_view, name='account_view'),
    
]   