from dataclasses import field, fields
from xml.parsers.expat import model
from django.core import validators
from django import forms
from django.forms import ModelForm
from  .models import items,supplier
from app import models

class ItemForm(forms.ModelForm):
    class Meta:
        model=items
        fields=['itemname','rate','brand']
        labels={
            'itemname':'Name',
            'rate': 'Rate',
            'brand':'Brand',
            # 'tdate':'Date',

        }
        widgets={
            'itemname':forms.TextInput(attrs={'class':'form-control'}),
            'rate':forms.TextInput(attrs={'class':'form-control'}),
            'brand':forms.TextInput(attrs={'class':'form-control'}),
            # 'tdate':forms.DateField(),
        }
    def __init__(self, *args, **kwargs):
        return super(ItemForm,self).__init__(*args, **kwargs)
        # self.fields['brand']
        # self.fields['tdate'].widget.attrs['readonly'] = True
class SupplierForm(forms.ModelForm):
    class Meta:
        model=supplier
        fields=['sname','email','password','address']
        labels={
            'sname':'Enter Name',
            'email': 'Enter Email',
            'password':'Password',
            'address':'Enter Address',

        }
        widgets={
            'sname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            
        }
    def __init__(self, *args, **kwargs):
        return super(SupplierForm,self).__init__(*args, **kwargs)
        # self.fields['sname']
        # self.fields['email'].widget.attrs['readonly'] = True
