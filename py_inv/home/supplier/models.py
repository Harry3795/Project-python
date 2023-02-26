from django.db import models

# Create your models here.
class SupplierMasterModel(models.Model):
    id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=200)
    mobile = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.IntegerField()
    status = models.SmallIntegerField(default=1)

    # class Meta:
    #     db_table = 'tbl_supplier_master'
    #     managed = False

    def __str__(self):
        return self.supplier_name

    def get_edit_url(self):
        return '/supplier/supplier_master/{}/{}'.format('Update', self.id)
