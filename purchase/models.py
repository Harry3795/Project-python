from django.db import models

# Create your models here.

class Purchase_MasterModel(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_no = models.CharField(max_length=200)
    invoice_date = models.DateField()
    supplier= models.ForeignKey('SupplierMasterModel', on_delete=models.CASCADE)   
    status = models.SmallIntegerField(default=1)
    
    class Meta:
        db_table = 'tbl_purchase_master'
        managed = False

    def __str__(self):
        return self.invoice_no
    
    # def get_read_url(self):
    #     return '/purchase/purchase_view/{}/{}'.format('Read', self.id)


class Purchase_DetailsModel(models.Model):
    id = models.AutoField(primary_key=True)
    purchase_master_id = models.IntegerField()
    item_id = models.IntegerField()
    qty = models.IntegerField()  
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)

    # class Meta:
    #     db_table = 'tbl_purchase_details'
    #     managed = False

    def __str__(self):
        return self.purchase_master_id

class SupplierMasterModel(models.Model):
    id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=200)
    mobile = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.IntegerField()
    status = models.SmallIntegerField(default=1)

    class Meta:
        db_table = 'tbl_supplier_master'
        managed = False

    def __str__(self):
        return self.supplier_name

class ItemMasterModel(models.Model):
    id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=200)
    item_name = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=200)
    status = models.SmallIntegerField(default=1)
    rate = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        db_table = 'tbl_items_master'
        managed = False

    def __str__(self):
        return self.item_name

class Purchase_tempModel(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey('ItemMasterModel', on_delete=models.CASCADE)   
    qty = models.IntegerField()  
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        db_table = 'tbl_temp_purchase'
        managed = False

class PurchaseDetailsModel(models.Model):
    id = models.AutoField(primary_key=True)
    purchase_master = models.ForeignKey('Purchase_MasterModel', on_delete=models.CASCADE)
    item = models.ForeignKey('ItemMasterModel', on_delete=models.CASCADE) 
    qty = models.IntegerField()  
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        db_table = 'tbl_purchase_details'
        managed = False

    def __str__(self):
        return str(self.rate) 
 