from django.urls import path
from .views import (
    product_create_view,
    product_detail_view,
    product_delete_view,
    product_list_view,
    product_update_view,
    dynamic_lookup_view,
)

urlpatterns = [
    path('product/', product_detail_view),
    path('products/<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('create/', product_create_view, name='product-create'),
    path('update/<int:id>/', product_update_view, name='product-update'),
    path('list/', product_list_view, name='product-list'),
    path('delete/<int:id>/', product_delete_view, name='product-delete'),
]
