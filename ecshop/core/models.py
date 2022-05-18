from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe



# Create your models here.

#Category
class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="cat_imgs/", null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = '1.Category'

    def image_tags(self):
        return mark_safe('<img src="%s" width="50" height="50">' %(self.image.url))

    def __str__(self):
        return self.title


#Product
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField()
    active = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True, null=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '2.Product'

    def get_cat_title(self):
        return self.category.title

    def __str__(self):
        return u"Id:{}, Name: {}".format(self.id, self.title) 

#product_Image 
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="pro_imgs/")

    class Meta:
        verbose_name_plural = '2.1.Product Attributes'
        
    def image_tags(self):
        return mark_safe('<img src="%s" width="50" height="50">' %(self.image.url))

    


#address
class Address(models.Model):
    address = models.TextField(blank=True) 


#Customer
class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    dateOfBirth = models.DateField(null=True)
    email = models.EmailField(null=True)
    active = models.BooleanField(default=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '3.Customers'


#Banner
class Banner(models.Model):
    image = models.ImageField(upload_to='banner_imgs')
    alt_text = models.CharField(max_length=255, null=True)


#Slider
class Slider(models.Model):
    image = models.ImageField(upload_to='slider_imgs')

#News
class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="news_imgs")
    content = models.TextField(blank=True)
    article = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = '6.News'


#FeedBack
class Feedback(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    rate = models.IntegerField(default=0)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)

#Favorite
class Favorite(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    act = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = '6.Favourite'



#Order
class Order(models.Model):
    qty = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = '4.Order'

    def __str__(self):
        return u"{} {} {}".format(self.id, self.total, self.created_date)


#Order detail
class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    qty = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image = models.ImageField(upload_to="detail_order_imgs",null=True)
    
    class Meta:
        verbose_name_plural = '5.Order Detail'











