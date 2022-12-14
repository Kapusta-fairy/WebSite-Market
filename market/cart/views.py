from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import DetailView
from shop.models import Products, Categories
from .cart import Cart
from .forms import SellForm, CartAddProductForm
from .models import Payment, Delivery, Politics


class PoliticCart(DetailView):
    model = Politics

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        return context


@require_POST
def cart_add(request, id):
    product = get_object_or_404(Products, id=id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        Cart(request).add_or_refresh(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('detail', product.slug)


def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=id)
    cart.remove(product)
    return redirect('cart')


def cart_detail(request):
    context = {'cart': Cart(request),
               'total': Cart(request).get_total_price(),
               'title': 'Корзина',
               'payment': Payment.objects.all(),
               'delivery': Delivery.objects.all(),
               'form': SellForm,
               'categories': Categories.objects.all()
               }
    return render(request, 'cart/detail.html', context)
