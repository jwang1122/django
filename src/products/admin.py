from django.contrib import admin

# Register your models here.
from .models import Product # relative import

admin.site.register(Product)