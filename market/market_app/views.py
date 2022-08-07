from django.views.generic import ListView, DetailView
from market_app.models import Products, Politics, Search, Basket, Detail


class PromoteMarketApp(ListView):
    """показывает самые популярные товары"""
    model = Products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = 'Предложения'
        return context


class PoliticMarketApp(DetailView):
    model = Politics


class SearchMarketApp(ListView):
    model = Search


class BasketMarketApp(ListView):
    model = Basket


class DetailMarketApp(DetailView):
    model = Detail
