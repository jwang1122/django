from django.urls import path
from .views import(
    BlogListView2,
)

app_name = 'blogs'
urlpatterns = [
    path('blog2/',BlogListView2.as_view(), name='blog-list'),
]