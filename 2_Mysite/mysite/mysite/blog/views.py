from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    obj=Post.objects.all()
    return render(request,'index.html',{'obj':obj})

def signup(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    if request.method=='POST':
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('blog:home')
        else:
            return redirect('blog:login')

    return render(request,'login.html')
