from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']


class RawProductForm(forms.Form):
    title = forms.CharField(label='Enter title',required=True, max_length=80)
    description = forms.CharField(
        required=False, 
        max_length=100, 
        label='',
        widget=forms.Textarea(
            attrs={
                "placeholder":"Your description",
                "row":20,
                "col": 100,
            }))
    price = forms.DecimalField(max_digits=10, decimal_places=2)
