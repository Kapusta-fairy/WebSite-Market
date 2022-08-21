from django.views.generic import CreateView
from review.forms import ReviewForm
from shop.models import Review


class CreateReview(CreateView):
    model = Review
    form_class = ReviewForm
    product = None

    def dispatch(self, request, *args, **kwargs):
        self.product = kwargs.get('product_slug')
        super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['course'] = self.product
        return kwargs
