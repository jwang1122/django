from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField(label='Enter title',required=True, max_length=80)
    class Meta:
        model = Book
        fields = ['title','description','price']

