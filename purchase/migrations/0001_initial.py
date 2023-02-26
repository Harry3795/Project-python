# Generated by Django 4.1 on 2022-08-28 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemMasterModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=200)),
                ('item_name', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('image', models.CharField(max_length=200)),
                ('status', models.SmallIntegerField(default=1)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_DetailsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_master_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_MasterModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_no', models.CharField(max_length=200)),
                ('invoice_date', models.DateField()),
                ('status', models.SmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierMasterModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=200)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('pincode', models.IntegerField()),
                ('status', models.SmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseDetailsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.itemmastermodel')),
                ('purchase_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.purchase_mastermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_tempModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.itemmastermodel')),
            ],
        ),
        migrations.AddField(
            model_name='purchase_mastermodel',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.suppliermastermodel'),
        ),
    ]
