from django.urls import path
from .views import( # CRUD: Create, Retrieve(detail, list), Update, Delete
    BlogCreateView,
    BlogDeleteView,
    BlogDetailView,
    BlogListView2,
    BlogUpdateView,
)

app_name = 'blogs'
urlpatterns = [
    path('',BlogListView2.as_view(), name='blog-list'),
    path('<int:id>/',BlogDetailView.as_view(), name='blog-detail'),
    path('create/',BlogCreateView.as_view(), name='blog-create'),
    path('<int:id>/update/',BlogUpdateView.as_view(), name='blog-update'),
    path('<int:id>/delete/',BlogDeleteView.as_view(), name='blog-delete'),
]