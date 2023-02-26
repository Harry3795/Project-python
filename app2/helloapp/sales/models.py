from django.db import models

# Create your models here.
class Sales_MasterModel(models.Model):
    id = models.AutoField(primary_key=True)
    sales_no = models.CharField(max_length=200)
    sales_date = models.DateField()
    customer_name = models.CharField(max_length=200) 
    mobile = models.IntegerField(max_length=200)
    address = models.CharField(max_length=200)    
    status = models.SmallIntegerField(default=1)
    
    class Meta:
        db_table = 'tbl_sales_master'
        managed = False

    def __str__(self):
        return self.sales_no
    
    def get_read_url(self):
        return '/sales/sales_view/{}/{}'.format('Read', self.id)

    

class SalesDetailsModel(models.Model):
    id = models.AutoField(primary_key=True)
    sales_master_id = models.IntegerField()
    item_id = models.IntegerField()
    qty = models.IntegerField()  
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        db_table = 'tbl_sales_details'
        managed = False

    def __str__(self):
        return self.rate

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

class Sales_tempModel(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey('ItemMasterModel', on_delete=models.CASCADE)   
    qty = models.IntegerField()  
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        db_table = 'tbl_temp_sales'
        managed = False

class SalesDetailsModel(models.Model):
    id = models.AutoField(primary_key=True)
    sales_master = models.ForeignKey('Sales_MasterModel', on_delete=models.CASCADE)
    item = models.ForeignKey('ItemMasterModel', on_delete=models.CASCADE) 
    qty = models.IntegerField()  
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        db_table = 'tbl_sales_details'
        managed = False

    def __str__(self):
        return str(self.rate)