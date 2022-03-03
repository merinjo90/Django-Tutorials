from django.shortcuts import render
from django import urls
from .models import *

# Create your views here.

def home(request):

    return render(request,'home.html')


def about(request):
    return render(request,'about.html')

def myservice(request):
    return render(request,'myservice.html')


def project(request):
    return render(request,'project.html')


def contact(request):
    if request.method=='POST':
        name = request.POST['name'],
        email = request.POST['email'],
        phone = request.POST['phone'],
        concern = request.POST['concern']
        obj=Contact(name=name,email=email,phone=phone,concern=concern)
        print(obj)
        obj.save()
    return render(request,'contact.html')

