from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from shop.forms import CartAddProductForm
from shop.models import Products, Politics


class PromoteShop(ListView):
    """показывает самые популярные товары"""
    model = Products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = 'Предложения'
        return context


class DetailShop(DetailView):
    model = Products


def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    form = CartAddProductForm()
    return render(request, 'shop/products_detail.html', {'product': product, 'form': form})


class PoliticShop(DetailView):
    model = Politics
