from django.urls import path
from .views import PromoteMarketApp, PoliticMarketApp
from . import views

urlpatterns = [
    path('', PromoteMarketApp.as_view(), name='promout'),
    path('politics/', PoliticMarketApp.as_view(), name='politics'),
    path('detail/<slug:slug>/', views.detail_product, name='detail'),
]
