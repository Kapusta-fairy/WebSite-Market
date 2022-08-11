from django.urls import path
from . import views
from .views import PromoteShop, PoliticShop

urlpatterns = [
    path('', PromoteShop.as_view(), name='promout'),
    path('politics/', PoliticShop.as_view(), name='politics'),
    path('detail/<slug:slug>/', views.product_detail, name='detail'),
]
