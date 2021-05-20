from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog_list_view(request):
    queryset =  Blog.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request, "blogs/blogs_list_view.html", context)
