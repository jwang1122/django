from django.urls import path
from .views import(
    BlogDetailView,
    BlogListView2,
    BlogCreateView,
    BlogUpdateView,
)

app_name = 'blogs'
urlpatterns = [
    path('',BlogListView2.as_view(), name='blog-list'),
    path('<int:id>/',BlogDetailView.as_view(), name='blog-detail'),
    path('create/',BlogCreateView.as_view(), name='blog-create'),
    path('<int:id>/update/',BlogUpdateView.as_view(), name='blog-update'),
]