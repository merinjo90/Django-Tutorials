from django.shortcuts import render
from .models import new_user

# Create your views here.

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pincode=request.POST.get('pincode')
        phone_no=request.POST.get('phone_no')
        job=request.POST.get('job')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1 == pass2:
            new_user(username=username,email=email,pincode=pincode,phone_no=phone_no,job_type=job,password=pass1).save()
    return render(request,'reg.html')
