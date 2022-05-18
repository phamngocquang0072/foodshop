from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('pro-detail/<int:id>/', productdetail, name='shop-detail'),
    path('shop-cat/<int:cat_id>/', shop_cat, name='shop-cat'),
    path('checkout/',checkout, name='checkout'),
    path('search',search, name='search'),
    path('add-to-cart',add_to_cart, name='add_to_cart'),
    path('shop-cart/',cart, name='shop-cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)