from django.urls import path
from review.views import CreateReview, add_review

urlpatterns = [
    path('review_add/<slug:slug>', add_review, name='review_add')
]
