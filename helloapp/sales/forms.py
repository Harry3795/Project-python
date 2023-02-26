from django import forms
from sales.models import *
from django.db.models import Subquery
from django.http import HttpResponse
import datetime

class salesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(salesForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control-input'

        self.fields['sales_no'].required = True
        self.fields['customer_name'].required = True
        self.fields['mobile'].required = True
        self.fields['address'].required = True
        self.fields['sales_date'].widget.attrs['class'] = 'form-control-input datepicker'
        # self.fields['invoice_date'].required = True
        sales_date = forms.DateField(input_formats=['%m/%d/%Y'], widget=forms.widgets.DateInput(format="%m/%d/%Y"), required=False)
        
        
    class Meta:
        model = Sales_MasterModel
        fields = ['sales_no','sales_date','customer_name','mobile','address']
        labels = {
            'sales_no': "Sales Number",
            'sales_date': "Sale Date",
            'customer_name': "Customer Name",
            'mobile': "Custoomer Mobile",
            'address': "Customer Address",
        }
 
class salesDetailsForm(forms.ModelForm):   
    def __init__(self, *args,**kwargs):
        super(salesDetailsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control-input'     
        
        self.fields['item_id'] = forms.ModelChoiceField(queryset=ItemMasterModel.objects.filter(status=1).order_by('id'), widget=forms.Select(attrs={"onChange":'getItems_data()'}))
        self.fields['rate'].required=True
        # self.fields['qty'] = forms.CharField(widget=forms.TextInput(attrs={'onchange': "calculate()",'onkeyup': "calculate()",'onkeypress': "isNumber(event)"}), required=True)
        self.fields['qty'].required=True
        self.fields['total'].required = True

    class Meta:
        model = SalesDetailsModel
        fields = ['rate','qty','total']

