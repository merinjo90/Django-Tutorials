from django.shortcuts import render
from django import urls

# Create your views here.

def home(request):

    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


def project(request):
    return render(request,'project.html')


def contact(request):
    return render(request,'contact.html')