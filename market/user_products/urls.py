from django.urls import path
from .views import CreateUserProducts, ShowUserProducts, product_remove, EditUserProducts

urlpatterns = [
    path('<int:pk>', ShowUserProducts.as_view(), name='user_products'),
    path('create/', CreateUserProducts.as_view(), name='create'),
    path('remove/<int:pk>', product_remove, name='product_remove'),
    path('edit/<slug:slug>/', EditUserProducts.as_view(), name='product_edit')
]
