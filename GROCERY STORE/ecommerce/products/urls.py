from django.contrib import admin
from django.urls import path
from .views import *

# from . import views

# app_name = "products"

urlpatterns = [
    path('products' , ProductView.as_view() ),
    path('demo',DemoView.as_view())
]
