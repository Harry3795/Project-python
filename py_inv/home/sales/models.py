from django.db import models
from .models import *

# Create your models here.
class Sales_MasterModel(models.Model):
    id = models.AutoField(primary_key=True)
    sales_no = models.CharField(max_length=200)
    sales_date = models.DateField()
    customer_name = models.CharField(max_length=200) 
    address = models.CharField(max_length=200)    
    status = models.SmallIntegerField(default=1)
    

    def __str__(self):
        return self.sales_no
    
    def get_read_url(self):
        return '/sales/sales_view/{}/{}'.format('Read', self.id)

    


class Sales_tempModel(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey('items.ItemMasterModel', on_delete=models.CASCADE)   
    qty = models.IntegerField()  
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)


class SalesDetailsModel(models.Model):
    id = models.AutoField(primary_key=True)
    sales_master = models.ForeignKey('Sales_MasterModel', on_delete=models.CASCADE)
    item = models.ForeignKey('items.ItemMasterModel', on_delete=models.CASCADE) 
    qty = models.IntegerField()  
    av_qty=models.IntegerField(null=True)
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self):
        return str(self.rate)