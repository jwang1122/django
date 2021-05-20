from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.

# def product_create_view(request):
#     form = RawProductForm()
#     if request.method=='POST':
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#             form = RawProductForm()
#         else:
#             print(form.errors)
#     context = {
#         "form":form
#     }
#     return render(request, "products/product_create.html",context)

# Original way to get user input values back
# def product_create_view(request):
#     # print(request.POST)
#     if request.method=='POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         price = request.POST.get('price')
#         Product.objects.create(title=title, description=description, price=price)
#     context = {}
#     return render(request, "products/product_create.html",context)

# using Django Form include values validation
def product_create_view(request):
    initial_data = {
        'title':'My awesome title',
        'price':10.99,
        'email':'wangqianjiang@live.edu'
    }
    form = ProductForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form':form
    }
    return render(request, "products/product_create.html",context)

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

def product_list_view(request):
    queryset =  Product.objects.all()
    # queryset =  Product.objects.all()[:5]
    # queryset =  Product.objects.filter(id=10)
    # queryset =  Product.objects.filter(title__contains='CFE')
    # queryset =  Product.objects.filter(id__gte=4)
    context = {
        "object_list":queryset
    }
    return render(request, "products/product_list.html", context)

def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=_id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    # obj = get_object_or_404(Product, id=_id)
    context = {
        'object':obj
    }
    return render(request, "products/product_lookup.html",context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method =='POST':
        obj.delete()
        return redirect('/products')
    context = {
        'object':obj
    }
    return render(request, "products/product_delete.html",context)

def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.id= id
            form.save()
            return redirect('/products')
    context = {
        'form':form
    }
    return render(request, "products/product_create.html",context)

