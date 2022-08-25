from django import template
from django.shortcuts import get_object_or_404
from shop.models import Products

register = template.Library()


@register.simple_tag()
def get_product_name(item):
    return get_object_or_404(Products, id=item['product_id']).name


@register.simple_tag()
def get_product_photo(item):
    return get_object_or_404(Products, id=item['product_id']).photo.url


@register.simple_tag()
def get_product_price(item):
    product = get_object_or_404(Products, id=item['product_id'])
    if product.discount:
        price = product.discount
    else:
        price = product.price
    return price
