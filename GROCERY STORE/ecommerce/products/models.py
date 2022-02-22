from django.db import models
from django.utils.text import slugify

from .views import *

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,blank=True)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.category_name


class QuantityVariant(models.Model):
    varient_name=models.CharField(max_length=200)

    def __str__(self):
        return self.varient_name

class ColorVarient(models.Model):
    color_name=models.CharField(max_length=200)
    color_code=models.CharField(max_length=200)

    def __str__(self):
        return self.color_name

class SizeVarient(models.Model):
    size_name=models.CharField(max_length=200)

    def __str__(self):
        return self.size_name


class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='static/products')
    stock=models.IntegerField(default=100)
    price=models.CharField(max_length=100)
    description=models.TextField()

    quantity_type=models.ForeignKey(QuantityVariant,blank=True,null=True,on_delete=models.PROTECT)
    color_type=models.ForeignKey(ColorVarient,blank=True,null=True,on_delete=models.PROTECT)
    size_type=models.ForeignKey(SizeVarient,blank=True,null=True,on_delete=models.PROTECT)


    def __str__(self):
        return self.product_name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    image=models.ImageField(upload_to='static/products')

