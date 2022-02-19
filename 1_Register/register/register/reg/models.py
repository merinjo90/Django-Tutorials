from django.db import models

# Create your models here.

class new_user(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    pincode=models.CharField(max_length=200)
    phone_no=models.CharField(max_length=200)
    job_type=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
