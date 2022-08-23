from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView
from review.forms import ReviewForm
from shop.models import Review, Products


class CreateReview(CreateView):
    form_class = ReviewForm
    product = None

    def dispatch(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        self.product = get_object_or_404(Products, slug=slug)
        super().dispatch(request, *args, **kwargs)
        return redirect('detail', slug)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['product'] = self.product
        return kwargs


def list_review(request, slug):
    product = get_object_or_404(Products, slug=slug)
    context = {'reviews': Review.objects.filter(product_id=product.id),
               'product_name': product.name}
    return render(request, 'shop/review_list.html', context)
