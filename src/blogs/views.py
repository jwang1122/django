from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .forms import BlogForm
from .models import Blog

class BlogCreateView(CreateView):
    template_name = 'blogs/blog_create.html' 
    form_class = BlogForm
    queryset =  Blog.objects.all() 
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class BlogDetailView(DetailView):
    template_name = 'blogs/blog_detail.html' # override default template file name
    # queryset =  Blog.objects.all() # look for: <app>/<modelname>_<view>.
    
    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Blog, id=_id)
    
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
