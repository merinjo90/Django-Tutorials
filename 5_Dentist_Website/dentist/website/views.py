from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request,'website/home.html')

def about(request):
    return render(request,'website/about.html')

def service(request):
    return render(request,'website/service.html')

def pricing(request):
    return render(request,'website/pricing.html')

def blog(request):
    return render(request,'website/blog.html')

def blog_details(request):
    return render(request,'website/blog_details.html')

def contact(request):
    if request.method=='POST':
        message_name=request.POST['message_name']
        message_email=request.POST['message_email']
        message=request.POST['message']

        #send an Email
        send_mail(
            message_name, #subject
            message,    #message
            message_email,  #from email
            ['merinjo90@gmail.com'],    #To Email
        )

        return render(request,'website/contact.html',{'message_name':message_name,'message_email':message_email,'message':message})
    else:
        return render(request,'website/contact.html')

def appointment(request):
    if request.method=='POST':
        your_name=request.POST['your_name'],
        your_phone=request.POST['your_phone'],
        your_email=request.POST['your_email'],
        your_address=request.POST['your_address'],
        your_schedule = request.POST['your_schedule'],
        your_date=request.POST['your_date'],
        your_message=request.POST['your_message']

        return render(request,'website/appointment.html', {
            'your_name':your_name,
            'your_phone':your_phone,
            'your_email':your_email,
            'your_address':your_address,
            'your_schedule':your_schedule,
            'your_date': your_date,
            'your_message':your_message
        })
    else:
        return render(request,'website/home.html',{})