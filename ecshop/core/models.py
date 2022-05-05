from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _



# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="imgs/cat_imgs/")
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="imgs/pro_imgs/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField()
    active = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return u"Id:{}, Name: {}".format(self.id, self.title) 

class Order(models.Model):
    qty = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return u"{} {} {}".format(self.id, self.total, self.created_date)

class Address(models.Model):
    address = models.TextField(blank=True) 

class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    dateOfBirth = models.DateField(null=True)
    email = models.EmailField(null=True)

class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Banner(models.Model):
    image = models.ImageField(upload_to='imgs/banner_imgs')
    alt_text = models.CharField(max_length=255)

class Slider(models.Model):
    image = models.ImageField(upload_to='imgs/slider_imgs')

class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="imgs/news_imgs")
    content = models.TextField(blank=True)
    article = models.CharField(max_length=255)

class Feedback(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    rate = models.IntegerField(default=0)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Favorite(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    act = models.BooleanField(default=False)











