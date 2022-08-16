from django.urls import path
from . import views
from .views import PromoteShop, SearchShop, CategoryShop

urlpatterns = [
    path('', PromoteShop.as_view(), name='promout'),
    path('detail/<slug:slug>/', views.product_detail, name='detail'),
    path('category/<slug:slug>/', CategoryShop.as_view(), name='category'),
    path('search/', SearchShop.as_view(), name='search')
]
