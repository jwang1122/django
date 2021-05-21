from django.urls import path
from .views import(
    BlogDetailView,
    BlogListView2,
)

app_name = 'blogs'
urlpatterns = [
    path('',BlogListView2.as_view(), name='blog-list'),
    path('<int:id>/',BlogDetailView.as_view(), name='blog-detal'),
]