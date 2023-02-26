from django.db import models

# Create your models here.

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

    def get_edit_url(self):
        return '/items/items_master/{}/{}'.format('Update', self.id)

