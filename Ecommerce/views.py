from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Products, Cart
from django.db.models import Sum 

def index(request):
    cart_item = Cart.objects.all()
    products = Products.objects.all()
    categories = Category.objects.all().order_by('name')
    return render(request, 'pages/index.html', {'products':products, 'cart_item':cart_item, 'categories':categories})

def details(request, id):
    cart_item = Cart.objects.all()
    detail = get_object_or_404(Products, id=id)
    products = Products.objects.filter(category_id=detail.category)
    products = [x for x in products if x.id != detail.id]
    return render(request, 'pages/details.html', {'detail':detail, 'products':products, 'cart_item':cart_item})


def cart(request):
    cart_item = Cart.objects.all()
    total = Cart.objects.all().aggregate(Sum('product__value'))
  
    return render(request, 'pages/cart.html', {'cart_item':cart_item, 'total':total['product__value__sum']})    

def add_cart(request, id):
    owner_cart = Cart.objects.filter(user_id=request.user.id)
    get_product = get_object_or_404(Products,id=id)

    if owner_cart:
        owner_cart = get_object_or_404(Cart, user_id=request.user.id)
        owner_cart.product.add(get_product)
    else:
        create_cart = Cart.objects.create(user_id=request.user.id)
        create_cart.product.add(get_product)
        owner_cart = create_cart
    

  
    cart_item = owner_cart.product
    products = Products.objects.all()
    categories = Category.objects.all().order_by('name')
    return render(request, 'pages/cart_item.html', {'products':products, 'cart_item':cart_item, 'categories':categories})
