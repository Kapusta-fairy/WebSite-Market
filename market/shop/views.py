from django.shortcuts import render
from django.views.generic import ListView, DetailView
from shop.models import Products, Politics


class PromoteMarketApp(ListView):
    """показывает самые популярные товары"""
    model = Products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = 'Предложения'
        return context


def detail_product(request):
    model = Products.all
    context = {
        'cart': cart,
        'title': 'корзина'
    }
    return render(request, template_name='cart/detail.html', context=context)


class PoliticMarketApp(DetailView):
    model = Politics
