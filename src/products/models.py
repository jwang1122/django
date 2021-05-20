from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={'id':self.id}) # clean and easy way to make url dynamic
        # return f"/products/{self.id}"
    
    def get_update_url(self):
        return reverse("products:product-update", kwargs={'id':self.id}) # clean and easy way to make url dynamic

    def get_delete_url(self):
        return reverse("products:product-delete", kwargs={'id':self.id}) # clean and easy way to make url dynamic
