from django.shortcuts import get_object_or_404

from market import settings
from shop.models import Products


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        for item in self.cart.values():
            item['price'] = float(item['price'])
            product = get_object_or_404(Products, id=item['product_id'])
            if product.discount:
                price = (product.discount * item['quantity'])
            else:
                price = (product.price * item['quantity'])
            item['total_price'] = price
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def add_or_refresh(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price),
                                     'product_id': product_id,
                                     'slug': product.slug}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        prices = []
        for item in self.cart.values():
            product = get_object_or_404(Products, id=item['product_id'])
            if product.discount:
                prices.append(product.discount * item['quantity'])
            else:
                prices.append(product.price * item['quantity'])
        return sum(prices)

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
