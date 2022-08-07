from django.urls import path
from .views import PromoteMarketApp, PoliticMarketApp, SearchMarketApp, BasketMarketApp, DetailMarketApp

urlpatterns = [
    path('', PromoteMarketApp.as_view(), name='promout'),
    path('politics/', PoliticMarketApp.as_view(), name='politics'),
    path('search/<slug:slug>/', SearchMarketApp.as_view(), name='search'),
    path('basket/', BasketMarketApp.as_view(), name='basket'),
    path('detail/<slug:slug>/', DetailMarketApp.as_view(), name='detail'),
]
