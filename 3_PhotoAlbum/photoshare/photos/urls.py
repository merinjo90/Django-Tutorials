from .views import *
from django.urls import path

urlpatterns=[
    path('',gallery,name='gallery'),
    path('photos/<str:pk>/', viewPhoto, name='photo'),
    path('add/', addPhoto, name='addPhoto'),

]