from django.views.generic import RedirectView
from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='base.html'),
    path(r'^favicon\.ico$',RedirectView.as_view(url='/static/blogs/favicon.ico')),
]