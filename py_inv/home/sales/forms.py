from django import forms
from sales.models import *
from django.db.models import Subquery
from django.http import HttpResponse
import datetime
from items.models import  *
from purchase.models import *

class salesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(salesForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control-input'

        self.fields['sales_no'].required = True
        self.fields['customer_name'].required = True
        self.fields['address'].required = True
        self.fields['sales_date'].widget.attrs['class'] = 'form-control-input datepicker'
        sales_date = forms.DateField(input_formats=['%m/%d/%Y'], widget=forms.widgets.DateInput(format="%m/%d/%Y"), required=False)
        
        
    class Meta:
        model = Sales_MasterModel
        fields = ['sales_no','sales_date','customer_name','address']
        labels = {
            'sales_no': "Sales Number",
            'sales_date': "Sale Date",
            'customer_name': "Customer Name",
            'address': "Customer Address",
        }
 
class salesDetailsForm(forms.ModelForm):   
    def __init__(self, *args,**kwargs):
        super(salesDetailsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control-input'     
        
        self.fields['item_id'] = forms.ModelChoiceField(queryset=PurchaseDetailsModel.objects.distinct('item_id').order_by('item_id'), widget=forms.Select(attrs={'onchange':"getItems_data();",'onchange':"getItems_av_qty();"}))
        self.fields['rate'].required=True
        # self.fields['qty'].widget=forms.Select(attrs={"onChange":'qtcheck()'})
        self.fields['qty'] = forms.CharField(widget=forms.TextInput(attrs={'onchange': "calculate()",'onchange': "isNumber(event)",'onchange':"qtcheck2()"}), required=True)
        self.fields['av_qty'].required=False
        self.fields['total'].required = True

    class Meta:
        model = SalesDetailsModel
        fields = ['rate','qty','av_qty','total']

