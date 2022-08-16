from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from shop.forms import CartAddProductForm
from shop.models import Products, Categories


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


class DetailShop(DetailView):
    model = Products


def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    form = CartAddProductForm()
    return render(request, 'shop/products_detail.html', {'product': product, 'form': form})
