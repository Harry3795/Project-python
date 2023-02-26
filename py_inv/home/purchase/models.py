from django.db import models
from items.models import *
from supplier.models import *

# Create your models here.

class Purchase_MasterModel(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_no = models.CharField(max_length=200)
    invoice_date = models.DateField()
    supplier= models.ForeignKey('supplier.SupplierMasterModel', on_delete=models.CASCADE)   
    status = models.SmallIntegerField(default=1)
 
    def __str__(self):
        return self.invoice_no
    
    def get_read_url(self):
        return '/purchase/purchase_view/{}/{}'.format('Read', self.id)





class Purchase_tempModel(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey('items.ItemMasterModel', on_delete=models.CASCADE)   
    qty = models.IntegerField()  
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)

 

class PurchaseDetailsModel(models.Model):
    id = models.AutoField(primary_key=True)
    purchase_master = models.ForeignKey('Purchase_MasterModel', on_delete=models.CASCADE)
    item = models.ForeignKey('items.ItemMasterModel', on_delete=models.CASCADE) 
    qty = models.IntegerField()  
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)

   
    def __str__(self):
        return str(self.item.item_name) 
    