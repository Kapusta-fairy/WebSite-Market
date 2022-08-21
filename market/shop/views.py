from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView
from shop.forms import CartAddProductForm, ReviewForm
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


class CreateReview(CreateView):
    model = Review
    form_class = ReviewForm

    def dispatch(self, request, *args, **kwargs):
        self.product = kwargs.get('product_slug')
        super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['course'] = self.product
        return kwargs


def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    context = {'product': product,
               'add_form': CartAddProductForm(),
               'review_form': ReviewForm(request.user, product)}
    return render(request, 'shop/products_detail.html', context)


def pay_plug(request):
    return HttpResponse('а, ну тут типа форма оплаты от банка, вот')


def review_add(request):
    pass
