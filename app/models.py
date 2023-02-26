from cgitb import enable
from email.policy import default
from enum import unique
from optparse import Option
from pickle import FALSE
from tkinter import CASCADE
from typing import Any
from xml.parsers.expat import model
from xmlrpc.client import boolean
from django.db import models



# Create your models here.
class p_form(models.Model):
    # sn=models.AutoField(("1"))
    itemname=models.CharField(max_length=255)
    rate=models.CharField(max_length=255)
    brand=models.CharField(max_length=255)
    date=models.DateField(blank=True,null=True,default='')
    status=models.IntegerField(default=1)
    def __str__(self):
        return self.itemname

class supplier(models.Model):
    sid=models.AutoField(primary_key=True,editable=FALSE,default=None)
    sname=models.CharField(max_length=255)
    semail=models.EmailField(max_length=35)
    smob=models.CharField(max_length=255)
    sadd=models.CharField(max_length=255)
    sdate=models.DateField(blank=True,null=True,default='')
    status=models.IntegerField(default=1)
    def __str__(self):
        return self.sname
class p_master(models.Model):
    pm_id=models.AutoField(primary_key=True,default=100)
    invoice=models.IntegerField()
    invoicedate=models.DateField(blank=True,null=True,default='')
    sname=models.CharField(max_length=50)
    sadd=models.TextField(max_length=255)
    status=models.IntegerField(default=1)
    def __str__(self):
        return self.invoice

class p_dtls(models.Model):
    pm_id=models.AutoField(primary_key=True,default=100)
    itemname=models.CharField(max_length=50)
    rate=models.IntegerField()
    qty=models.IntegerField()
    total=models.IntegerField()
    sid=models.ForeignKey(supplier,on_delete=callable,default='')
    status=models.IntegerField(default=1)
    def __str__(self):
        return self.itemname
class p_temp(models.Model):
    pm_id=models.AutoField(primary_key=True,default=100)
    itemname=models.CharField(max_length=50)
    rate=models.IntegerField()
    qty=models.IntegerField()
    total=models.IntegerField()
    sid=models.ForeignKey(supplier,on_delete=callable,default='')
    status=models.IntegerField(default=1)
    def __str__(self):
        return self.itemname
