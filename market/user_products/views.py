from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from shop.models import Products, Categories
from user_products.forms import ProductsForm


class CreateUserProducts(CreateView):
    form_class = ProductsForm
    template_name = 'user_products/products_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = 'Добавить товар'
        context['button'] = 'Добавить'
        context['categories'] = Categories.objects.all()
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ShowUserProducts(ListView):
    model = Products
    template_name = 'user_products/user_products_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Products.objects.filter(author=self.kwargs['pk'])
        context['Title'] = 'Мои товары'
        context['categories'] = Categories.objects.all()
        return context


class EditUserProducts(CreateView):
    form_class = ProductsForm
    template_name = 'user_products/products_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = 'Редактировать товар'
        context['button'] = 'Сохранить'
        context['categories'] = Categories.objects.all()
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


def product_remove(request, pk):
    Products.objects.filter(pk=pk).delete()
    return redirect('user_products', request.user.id)
