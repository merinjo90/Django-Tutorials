from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import PostForm

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
        confirm_password = request.POST.get('confirm_password')
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist')
                return redirect('blog:register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email already exist')
                return redirect('blog:register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request,user)
                messages.error(request, 'Sucess')
                return redirect('blog:register')
        else:
            messages.error(request, 'Password not equal')
            return redirect('blog:register')
    return render(request,'register.html')


def create_post(request):
    form =PostForm()
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form=PostForm()
    return render(request,'create_post.html',{'form':form})


def update_post(request,id):
    obj=Post.objects.get(id=id)
    form=PostForm(request.POST or None, instance=obj)
    if request.method=='POST':
        if form.is_valid():
            form.save()
    return render(request,'update_post.html',{form:'form'})