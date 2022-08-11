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
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    context = {
        'cart': cart,
        'title': 'корзина'
    }
    return render(request, template_name='cart/detail.html', context=context)


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)
    return redirect('cart')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


def product_detail(request, p_id, slug):
    product = get_object_or_404(Products,
                                id=p_id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})
