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
class BlogDetailView(DetailView):
    template_name = 'blogs/blog_detail.html' # override default template file name
    queryset =  Blog.objects.all() # look for: <app>/<modelname>_<view>.html
    
class BlogListView2(ListView):
    template_name = 'blogs/blog_list.html' # override default template file name
    queryset =  Blog.objects.all() # look for: <app>/<modelname>_<view>.html


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
