from django.urls import path

from .views import MainView, CategoryView

urlpatterns = [
    path('', MainView.as_view()),
    path('/categories', CategoryView.as_view()),
]