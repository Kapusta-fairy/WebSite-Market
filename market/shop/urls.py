from django.urls import path
from .views import PromoteShop, SearchShop, CategoryShop, product_detail, pay_plug, create_product

urlpatterns = [
    path('', PromoteShop.as_view(), name='promout'),
    path('detail/<slug:slug>/', product_detail, name='detail'),
    path('category/<slug:slug>/', CategoryShop.as_view(), name='category'),
    path('search/', SearchShop.as_view(), name='search'),
    path('plug/', pay_plug, name='plug'),
    path('create/', create_product, name='create'),
    # path('create/', CreateProduct.as_view(), name='create'),
]
