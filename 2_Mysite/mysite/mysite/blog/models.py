from django.db import models

# Create your models here.

class Post(models.Model):
    head=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.head