from django.db import models

# Create your models here.
class Blog(models.Model):
    topic = models.CharField(max_length=120)
    
