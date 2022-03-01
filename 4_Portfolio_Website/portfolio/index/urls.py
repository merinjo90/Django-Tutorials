
from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name='home'),
    # path('home', home, name='home'),
    path('about',about,name='about'),
    path('project', project, name='project'),
    path('contact', contact, name='contact'),

]