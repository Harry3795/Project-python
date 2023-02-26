from django import forms
from supplier.models import *
from django.db.models import Subquery


class supplierMasterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(supplierMasterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control-input'

        address= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20, "maxlength":'50'}), required=True)
        self.fields['supplier_name'].required = True
        #self.fields['mobile'].widget.attrs['maxlength'] = 10   
        self.fields['mobile']= forms.CharField(widget=forms.TextInput(attrs={"maxlength":'10','onkeypress': "isNumber(event)"}), required=True)
        self.fields['city'].required = True
        self.fields['state'].required = True
        self.fields['pincode'].required = True

    class Meta:
        model = SupplierMasterModel
        fields = ['supplier_name','mobile','address','city','state','pincode']
        labels = {
            'supplier_name': "Supplier Name",
            'mobile': "Mobile Number",
            'address': "Address",
            'city':"City",
            'state':"State",
            'pincode':"Pincode",
        }
        error_messages = {
            'supplier_name': {
                'required': 'Please Enter Supplier Name',
            },
            'mobile': {
                'required': 'Please Enter Mobile Number',
            },
            'address': {
                'required': 'Please Enter Address',
            },
            'city': {
                'required': 'Please Enter City',
            },
            'state': {
                'required': 'Please Enter State',
            },
            'state': {
                'required': 'Please Enter Pincode',
            },
        }

    
