from django.urls import path
# from blog import views
from .views import *

app_name='blog'

urlpatterns=[
    path('',home,name='home'),
    path('login/',signup,name='login'),
    path('logout',logout_user,name='logout')

]