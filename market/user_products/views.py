from django.contrib import messages
from django.shortcuts import redirect, render

from user_products.forms import ProductsForm


def create_product(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Отчёт отправлен')
            return redirect('promout')
        else:
            messages.error(request, 'Ошибка отправки отчёта')
    else:
        form = ProductsForm()
    return render(request, 'shop/create_product.html', {'form': form})
