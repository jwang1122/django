from django.urls import path
from .views import (
    # product_create_view,
    # product_detail_view,
    # product_delete_view,
    BookListView,
    # book_list_view,
    # product_update_view,
    # dynamic_lookup_view,
)

app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
#     path('<int:id>/',BlogDetailView.as_view(), name='blog-detail'),
#     path('create/',BlogCreateView.as_view(), name='blog-create'),
#     path('<int:id>/update/',BlogUpdateView.as_view(), name='blog-update'),
#     path('<int:id>/delete/',BlogDeleteView.as_view(), name='blog-delete'),
]
