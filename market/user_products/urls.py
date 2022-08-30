from django.urls import path
from .views import create_product

urlpatterns = [
    path('create/', create_product, name='create'),
]
