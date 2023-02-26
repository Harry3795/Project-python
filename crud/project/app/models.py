from django.db import models
from datetime import *


# Create your models here.
class items(models.Model):
    itemname=models.CharField(max_length=255)
    rate=models.CharField(max_length=255)
    brand=models.CharField(max_length=255)
    # tdate=models.DateField(auto_now_add=True,editable=True)
    # status=models.IntegerField(default=1)
    def __str__(self):
        return self.itemname
class supplier(models.Model):
    sname=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
   
    def __str__(self):
        return self.sname


