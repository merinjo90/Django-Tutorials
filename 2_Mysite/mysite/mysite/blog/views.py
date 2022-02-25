from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    obj = Post.objects.all()
    return render(request, 'index.html', {'obj': obj})


def signup(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if request.method == 'POST':
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:home')
        else:
            messages.error(request, 'User not exist.')
            return redirect('blog:login')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('blog:home')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(username,password,email)
        user=User.objects.create_user(username=username,email=email,password=password)
        login(request,user)
    return render(request, 'register.html')
