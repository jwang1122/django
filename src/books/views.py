from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Book

# Create your views here.
class BookListView(View):
    template_name = 'books/book_list.html' # override default template file name
    queryset =  Book.objects.all() # look for: <app>/<modelname>_<view>.html

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)