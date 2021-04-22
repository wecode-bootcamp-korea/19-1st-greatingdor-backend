from django.urls import path

from .views      import CartView

urlpatterns = [
    path("/<int:member_id>/<int:product_id>", CartView.as_view()),
]
