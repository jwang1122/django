from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    topic = models.CharField(max_length=120)
    
    def get_absolute_url(self):
        return reverse("blogs:blog-detail", kwargs={'id':self.id}) # clean and easy way to make url dynamic
