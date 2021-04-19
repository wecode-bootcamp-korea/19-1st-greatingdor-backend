from django.urls import path

from product_details.views import ProductDetailView

urlpatterns = [path("/marketDetail", ProductDetailView.as_view())]
