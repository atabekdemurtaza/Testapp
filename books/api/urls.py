from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path(
        route='books/',
        view=BookListCreateView.as_view(),
        name='book-list-create'),
    path(
        route='books/<int:pk>/',
        view=BookRetrieveUpdateDestroyView.as_view(),
        name='book-retrieve-update-destroy'),
]
