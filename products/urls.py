from django.urls import path

from .views                import MainView, CategoryView
from product_details.views import ProductDetailView, ProductOptionView, ProductReviewView

urlpatterns = [
    path("", MainView.as_view()),
    path("/<int:product_id>", ProductDetailView.as_view()),
    path("/categories", CategoryView.as_view()),
    path("/<int:product_id>/options", ProductOptionView.as_view()),
    path("/<int:product_id>/reviews", ProductReviewView.as_view()),
]
