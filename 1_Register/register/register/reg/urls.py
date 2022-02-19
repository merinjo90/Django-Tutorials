
from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from .import views

urlpatterns = [
    path('new_reg/',views.register,name='register'),
]