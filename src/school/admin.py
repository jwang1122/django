from django.contrib import admin

# Register your models here.
from .models import School # relative import

admin.site.register(School)