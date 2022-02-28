from django.urls import path
# from blog import views
from .views import *

app_name='blog'

urlpatterns=[
    path('',home,name='home'),
    path('login/',signup,name='login'),
    path('logout',logout_user,name='logout'),
    path('register/',register,name='register'),
    path('create_post/',create_post, name='create_post'),
    path('update_post/<int:id>',update_post, name='update_post')

]