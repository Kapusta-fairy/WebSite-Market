from django.urls import path
from review.views import CreateReview, list_review

urlpatterns = [
    path('review_add/<slug:slug>', CreateReview.as_view(), name='review_add'),
    path('reviews/<slug:slug>', list_review, name='reviews')
]
