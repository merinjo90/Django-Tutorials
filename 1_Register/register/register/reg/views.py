from django.shortcuts import render,redirect
from .models import new_user
from hashlib import sha256 #encrypted pswd

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
        password=sha256(pass2.encode()).hexdigest() #encrypted pwsd
        new_user(username=username,email=email,pincode=pincode,phone_no=phone_no,job_type=job,password=password).save()
    return render(request,'reg.html')


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        password2=sha256(password.encode()).hexdigest() #encrypted pwsd
        user=new_user.objects.get(username=username,password=password2)
        # user=new_user.objects.filter(username=username,password=password2)

        if user:
            user_details=new_user.objects.get(username=username,password=password2)
            id=user_details.id
            username_user=user_details.username
            request.session['id']=id
            request.session['username']=username_user
            return redirect('home')
        else:
            return redirect('login')


    return render(request,'login.html')

def home(request):
    id=request.session['id']
    username=request.session['username']
    return render(request,'home.html',{'id':id,'name':username})