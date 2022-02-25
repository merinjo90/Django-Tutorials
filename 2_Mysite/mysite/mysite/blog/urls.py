from django.urls import path
# from blog import views
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('login/',signup,name='login')

# path('',views.home,name='home'),
#     path('login/',views.signup,name='login')

]