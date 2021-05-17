from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text":"this is about us",
        "my_num":123,
        "my_list":[112146, 223531, 164323],
        "my_html":"<h1>Hello World!</h1>",
    }
    return render(request, "about.html",my_context)