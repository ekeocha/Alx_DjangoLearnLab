from django.urls import path
from .views import BookListCreateAPIView
from . import views

urlpatterns = [
    path("books", views.BookListCreateAPIView.as_view(), name="book_list_create"),
]