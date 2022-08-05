from django.views.generic import ListView, DetailView
from market_app.models import Products, Politics, Search, Basket, Detail


class PromouteMarketApp(ListView):
    model = Products


class PoliticMarketApp(DetailView):
    model = Politics


class SearchMarketApp(ListView):
    model = Search


class BasketMarketApp(ListView):
    model = Basket


class DetailMarketApp(DetailView):
    model = Detail
