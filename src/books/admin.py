from django.contrib import admin

# Register your models here.
from .models import Book # relative import

admin.site.register(Book)