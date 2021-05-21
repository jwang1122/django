from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    topic = forms.CharField(label='Enter title',required=True, max_length=80)
    class Meta:
        model = Blog
        fields = ['topic']

