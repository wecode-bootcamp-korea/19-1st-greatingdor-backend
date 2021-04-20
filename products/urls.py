from django.urls import path

from .views import MainView, CategoryView, SearchView

urlpatterns = [
    path('', MainView.as_view()),
    path('/categories', CategoryView.as_view()),
    path('/search', SearchView.as_view()),
]