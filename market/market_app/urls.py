from django.urls import path
from .views import PromoutMarketApp

urlpatterns = [
    path('', PromoutMarketApp.as_view(), name='promout'),
]
