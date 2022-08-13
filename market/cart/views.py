from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Products
from .cart import Cart
from shop.forms import CartAddProductForm


@require_POST
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add_or_refresh(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return render(request, 'cart/detail.html', {'cart': cart, 'title': 'корзина'})


def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=id)
    cart.remove(product)
    return redirect('cart')


def cart_detail(request):
    return render(request, 'cart/detail.html', {'cart': Cart(request)})
