from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.template.context_processors import csrf
from django.views.generic import CreateView
from review.forms import ReviewForm
from shop.models import Review, Products


class CreateReview(CreateView):
    model = Review
    form_class = ReviewForm
    product = None

    def dispatch(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        self.product = get_object_or_404(Products, slug=product_id)
        super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['product'] = self.product
        return kwargs


def add_review(request, slug):
    token = csrf(request)
    if request.POST:
        product = Products.objects.get(slug=slug)
        user_id = request.POST.get('userfromform', '')
        user = User.objects.get(id=user_id)
        form = ReviewForm(request.POST, product)
        if form.is_valid():
            review = form.cleaned_data['review']
            review_obj = Review(product=product, author=user, review=review)
            review_obj.save()
            return redirect('detail', token)
