from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.

def product_create_view(request):
    # print(request.POST)
    if request.method=='POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        Product.objects.create(title=title, description=description, price=price)
    context = {}
    return render(request, "products/product_create.html",context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()

#     context = {
#         'form':form
#     }
#     return render(request, "products/product_create.html",context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title':obj.title,
    #     'price':obj.price,
    # }
    context = {
        'object':obj
    }
    return render(request, "products/product_detail.html",context)