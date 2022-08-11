from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_detail, name='cart'),
    path('add/<int:id>', views.cart_add, name='cart_add'),
    path('remove/<slug:slug>', views.cart_remove, name='cart_remove'),
]
