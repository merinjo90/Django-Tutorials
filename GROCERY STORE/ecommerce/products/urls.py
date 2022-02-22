from django.contrib import admin
from django.urls import path,include
from .views import *

# from . import views

# app_name = "products"

urlpatterns = [
    path('products' , ProductView.as_view() ),
]
