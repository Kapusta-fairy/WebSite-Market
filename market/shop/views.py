from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView
from cart.cart import Cart
from cart.forms import CartAddProductForm
from review.forms import ReviewForm
from shop.forms import SaleForm
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
               'review_form': ReviewForm(request.user, product),
               'categories': Categories.objects.all()}
    return render(request, 'shop/products_detail.html', context)


class CreateProduct(CreateView):
    form_class = SaleForm
    template_name = 'shop/templates/shop/create_product.html'


def pay_plug(request):
    cart = Cart(request)
    slugs = []
    quantity = []
    for i in cart.cart:
        i = cart.cart[i]
        quantity.append(i['quantity'])
        slugs.append(i['slug'])
    for i in range(len(slugs)):
        product = get_object_or_404(Products, slug=slugs[i])
        product.total_purchased += quantity[i]
        product.save()
    cart.clear()
    return HttpResponse('а, ну тут типа форма оплаты от банка, вот')
