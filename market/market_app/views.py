from django.views.generic import ListView
from market_app.models import Offer


class PromoutMarketApp(ListView):
    model = Offer

