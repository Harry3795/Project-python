# Generated by Django 4.1 on 2022-08-28 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_alter_itemmastermodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='itemmastermodel',
            table='tbl_items_master',
        ),
        migrations.AlterModelTable(
            name='purchase_mastermodel',
            table='tbl_purchase_master',
        ),
        migrations.AlterModelTable(
            name='purchase_tempmodel',
            table='tbl_temp_purchase',
        ),
        migrations.AlterModelTable(
            name='purchasedetailsmodel',
            table='tbl_purchase_details',
        ),
        migrations.AlterModelTable(
            name='suppliermastermodel',
            table='tbl_supplier_master',
        ),
    ]
