from django.db import models

# Create your models here.
class School(models.Model):
    name = models.TextField()
    students = models.IntegerField()


    
