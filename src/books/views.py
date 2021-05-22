from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Book
from .forms import BookForm

# Create your views here.
class BookListView(View):
    template_name = 'books/book_list.html' # override default template file name
    queryset =  Book.objects.all() # look for: <app>/<modelname>_<view>.html

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

class BookDetailView(View):
    template_name = 'books/book_detail.html' # override default template file name

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Book, id=id)
            context["object"]=obj
        return render(request, self.template_name, context)

class BookCreateView(View):
    template_name = 'books/book_create.html' # override default template file name
    def get(self, request, *args, **kwargs):
        form = BookForm()
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form':BookForm()}
        return render(request, self.template_name,context)

    def get_success_url(self) -> str:
        return '/books'

class BookUpdateView(View):
    pass

class BookDeleteView(View):
    pass