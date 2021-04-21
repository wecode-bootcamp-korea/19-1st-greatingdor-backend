from django.urls import path

from .views                import MainView, CategoryView
from product_details.views import ProductDetailView, ProductOptionView

urlpatterns = [
    path("", MainView.as_view()),
    path("/<product_id>", ProductDetailView.as_view()),
    path("/categories", CategoryView.as_view()),
    path("/<product_id>/options", ProductOptionView.as_view()),
]
