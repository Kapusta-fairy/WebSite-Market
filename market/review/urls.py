from django.urls import path
from review.views import CreateReview

urlpatterns = [
    path('review_add/<slug:slug>', CreateReview.as_view(), name='review_add')
]
