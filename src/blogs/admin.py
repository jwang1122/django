from django.contrib import admin

# Register your models here.
from .models import Blog # relative import

admin.site.register(Blog)