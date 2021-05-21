from django.shortcuts import render
from .models import Blog
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

class BlogListView2(ListView):
    queryset =  Blog.objects.all() # look for: blog/modelname_list.html


class BlogListView(View):
    queryset =  Blog.objects.all()

    def get(self, request):
        context = {
            "object_list":self.queryset
        }
        return render(request, "blogs/blogs_list_view.html", context)

# Create your views here.
def blog_list_view(request):
    queryset =  Blog.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request, "blogs/blogs_list_view.html", context)
