from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    obj=Post.objects.get(id=1)
    return render(request,'index.html',{'obj':obj})
