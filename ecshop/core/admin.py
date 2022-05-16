from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title","image_tags","active")

class ProductAdmin(admin.ModelAdmin):
    list_display = ("title","price","get_cat_title","qty","active", "is_featured")
    
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "image_tags")



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Customer)
admin.site.register(Banner)
admin.site.register(Slider)
admin.site.register(Address)
admin.site.register(News)


