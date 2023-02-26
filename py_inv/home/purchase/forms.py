from django import forms
from purchase.models import *
from django.db.models import Subquery
from django.http import HttpResponse
import datetime
from items.models import *
from supplier.models import *


class purchaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(purchaseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control-input'

        self.fields['invoice_no'].required = False
        self.fields['invoice_date'].widget.attrs['class'] = 'form-control-input-date datepicker'
        invoice_date = forms.DateField(input_formats=['%m/%d/%Y'], widget=forms.widgets.DateInput(format="%m/%d/%Y"), required=False)
        self.fields['supplier_id']= forms.ModelChoiceField(
            queryset=SupplierMasterModel.objects.filter(status=1).order_by('id'), 
            widget=forms.Select(attrs={"onChange":'getSupplier_data()'}))

    class Meta:
        model = Purchase_MasterModel
        fields = ['invoice_no','invoice_date']
        labels = {
            'invoice_no': "Invoice Number",
            'invoice_date': "Invoice Date",
            'supplier_id': "Supplier",
        }
        error_messages = {
            'invoice_no': {
                'required': 'Please Enter Invoice Number',
            },
            'invoice_date': {
                'required': 'Please Select Invoice Date',
            },
            'supplier_id': {
                'required': 'Please Select Supplier Name',
            },
        }

class purchaseDetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(purchaseDetailsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control-input'
        
        self.fields['item_id'] = forms.ModelChoiceField(queryset=ItemMasterModel.objects.filter(status=1).order_by('id'), widget=forms.Select(attrs={"onChange":'getItems_data()'}))
        self.fields['rate'].required=True
        self.fields['qty'] = forms.CharField(widget=forms.TextInput(attrs={'onchange': "calculate()",'onchange': "calculate()",'onchange': "isNumber(event)"}), required=True)
        # self.fields['qty'].required=True
        self.fields['total'].required = True

    class Meta:
        model = PurchaseDetailsModel
        fields = ['rate','qty','total']


        

