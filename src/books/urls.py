from django.urls import path
from .views import (
    BookCreateView,
    BookDeleteView,
    BookListView,
    BookDetailView,
    BookUpdateView,
)

app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('<int:id>/',BookDetailView.as_view(), name='book-detail'),
    path('create/',BookCreateView.as_view(), name='book-create'),
    path('<int:id>/update/',BookUpdateView.as_view(), name='blog-update'),
    path('<int:id>/delete/',BookDeleteView.as_view(), name='blog-delete'),
]
