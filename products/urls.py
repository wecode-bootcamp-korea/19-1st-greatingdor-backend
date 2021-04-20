from django.urls import path

from .views                import MainView, CategoryView
from product_details.views import ProductDetailView

urlpatterns = [
    path("", MainView.as_view()),
    path("/categories", CategoryView.as_view()),
    path("/detail/<product_id>", ProductDetailView.as_view()),
]
