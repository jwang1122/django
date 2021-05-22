from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .models import Book
from .forms import BookForm

# Create your views here.
class BookListView(View):
    template_name = 'books/book_list.html' # override default template file name

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        queryset = Book.objects.all()
        context = {'object_list': queryset}
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
    template_name = 'books/book_update.html' # override default template file name

    def get_object(self):
        _id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Book, id=_id)
        return obj

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is not None:
            form = BookForm(instance=obj)
            context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is not None:
            form = BookForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('/books')
        return render(request, self.template_name,{})

class BookDeleteView(View):
    pass