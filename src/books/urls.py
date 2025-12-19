from django.urls import path
from .views import (
    BookListView,
    BookCreateView,
    BookUpdateDeleteView
)

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('create/', BookCreateView.as_view(), name='book-create'),
    path('<int:book_id>/', BookUpdateDeleteView.as_view(), name='book-update-delete'),
]
