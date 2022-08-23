from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from cart.cart import Cart
from cart.forms import CartAddProductForm
from review.forms import ReviewForm
from shop.models import Products, Categories, Review


class PromoteShop(ListView):
    model = Products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = 'Предложения'
        context['categories'] = Categories.objects.all()
        return context


class SearchShop(ListView):

    def get_queryset(self):
        return Products.objects.filter(name__icontains=self.request.GET.get('search'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        return context


class CategoryShop(ListView):

    def get_queryset(self):
        category = Categories.objects.get(slug=self.kwargs['slug'])
        return Products.objects.filter(category=category)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        return context


def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    context = {'product': product,
               'reviews': Review.objects.filter(product_id=product.id)[:3],
               'add_form': CartAddProductForm(),
               'review_form': ReviewForm(request.user, product)}
    return render(request, 'shop/products_detail.html', context)


def pay_plug(request):
    cart = Cart(request)
    slugs = []
    for i in cart.cart:
        i = cart.cart[i]
        slugs.append(i['slug'])
    for slug in slugs:
        product = get_object_or_404(Products, slug=slug)
        product.total_purchased += 1
        product.save()
    cart.clear()
    return HttpResponse('а, ну тут типа форма оплаты от банка, вот')
