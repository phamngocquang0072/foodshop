from django.shortcuts import render
from django.template.loader import render_to_string
from .models import *
from datetime import date
from django.db.models import Min, Max
from django.http import JsonResponse
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
def getCategory():
    return Category.objects.all().order_by('-id') 

def getProduct():
    return Product.objects.all().order_by('-id')

def getFeaturedProduct():
    return Product.objects.filter(is_featured=True).order_by('-id')

def getLatestProduct():
    return Product.objects.all().order_by('-id')[:4]
    
#filter product
def get_maxmin_filter(request):
    return Product.objects.aggregate(Min('price'), Max('price'))

#Home page

def home(request): 
    return render(request, 'index.html', {'cat': getCategory, 
                                          'pro':getProduct,
                                          'fpro':getFeaturedProduct, 
                                          'ltpro':getLatestProduct})

#shop page

def shop(request):
    count = Product.objects.all().count()
    return render(request, 'shop.html', {'cat': getCategory,
                                         'pro':getProduct, 
                                         'ltpro':getLatestProduct, 
                                         'count': count,
                                         'maxminfilter':get_maxmin_filter})

#shop page

def shop_cat(request, cat_id):
    cat = Category.objects.get(id=cat_id)
    product = Product.objects.filter(category = cat_id).order_by('-id')
    count = Product.objects.filter(category = cat_id).count()
    return render(request, 'shop_cat.html', {'cat': getCategory, 
                                             'cpro':product, 
                                             'ltpro':getLatestProduct, 
                                             'count': count, 
                                             'catdt':cat})

#detail

def productdetail(request,id):
    product = Product.objects.get(id = id)
    images = ProductImage.objects.filter(product=id)
    rkpro = Product.objects.filter(category=product.category).order_by('-id')
    return render(request, 'shop-details.html', {'pro': product, 
                                                 'ltpro':rkpro, 
                                                 'image':images })


#Search

def search(request):
    q = request.GET['q']
    spro = Product.objects.filter(title__icontains=q).order_by('-id')
    return render(request, 'search.html', {'spro': spro})

#add to cart 

def add_to_cart(request):
    cart = {}
    cart[str(request.GET['id'])]={
        'title': request.GET['title'],
        # 'image': request.GET['image'],
        'qty': request.GET['qty'],  
        'price': request.GET['price'],
        
    }
    

    if 'cartdata' in request.session:
        if str(request.GET['id']) in request.session['cartdata']:
            cartdata = request.session['cartdata']
            cartdata[str(request.GET['id'])]['qty']=str(int(cartdata[str(request.GET['id'])]['qty'])+int(cart[str(request.GET['id'])]['qty']))
            cartdata.update(cartdata)
            request.session['cartdata'] = cartdata
        else:
            cartdata = request.session['cartdata']
            cartdata.update(cart)
            request.session['cartdata'] = cartdata
    else:
        request.session['cartdata']=cart 

    return JsonResponse({'data':cart, 'total':len(request.session['cartdata'])})

# delete cart item

def delete_cart_item(request):
    p_id = str(request.GET['id'])
    if 'cartdata' in request.session:
        if p_id in request.session['cartdata']:
            cartdata = request.session['cartdata']
            del request.session['cartdata'][p_id]
            request.session['cartdata'] = cartdata
    
    total=0
    cart = request.session.get('cartdata',{})
    for p_id, item in cart.items():
        total += int(item['qty'])*float(item['price'])

    t = render_to_string('ajax/cart-list.html',{'cart': cart,
                                                 'total':len(cart),
                                                 'total1': total,
                                                 })
    return JsonResponse({'data':t})

# delete cart item

def update_cart_item(request):
    
    
    p_id = str(request.GET['id'])
    p_qty = request.GET['qty']
    if 'cartdata' in request.session:
        if p_id in request.session['cartdata']:
            cartdata = request.session['cartdata']
            cartdata[str(request.GET['id'])]['qty']=p_qty
            request.session['cartdata'] = cartdata
    cart = request.session.get('cartdata',{})
    total=0
    for p_id, item in cart.items():
        total += int(item['qty'])*float(item['price'])
    return render(request, 'shoping-cart.html', {'cart': cart,
                                                 'total':len(cart),
                                                 'total1': total,
                                                 })


# cart

def cart(request):
    total=0
    cart = request.session.get('cartdata',{})
    for p_id, item in cart.items():
        total += int(item['qty'])*float(item['price'])
    return render(request, 'shoping-cart.html', {'cart': cart,
                                                 'total':len(cart),
                                                 'total1': total,
                                                 })

# #login & register

# def login(request):
#     return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            user=authenticate(username = username,password = pwd)
            login(request, user)
            return redirect('home')
        
    form = SignupForm
    return render(request, 'registration/register.html', {'form': form})


#checkout
@login_required
def checkout(request):
    total=0
    if 'cartdata' in request.session:
        cart = request.session.get('cartdata')
        for p_id, item in cart.items():
            total += int(item['qty'])*float(item['price'])
        return render(request, 'checkout.html', {'cart': cart,
                                                 'total':len(cart),
                                                 'total1': total,
                                                 })

    

