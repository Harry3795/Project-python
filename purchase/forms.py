from django import forms
from purchase.models import *
from django.db.models import Subquery
from django.http import HttpResponse
import datetime

class purchaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(purchaseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control-input'

        self.fields['invoice_no'].required = True
        self.fields['invoice_date'].widget.attrs['class'] = 'form-control-input-date datepicker'
        # self.fields['invoice_date'].required = True
        invoice_date = forms.DateField(input_formats=['%m/%d/%Y'], widget=forms.widgets.DateInput(format="%m/%d/%Y"), required=False)
        # self.fields['supplier_id'].required = True
        # self.fields['supplier_id'].queryset=SupplierMasterModel.objects.filter(status=1).order_by('id')
        # self.fields['supplier_id'].empty_label = '------ Please Select ------'     
        # self.fields['supplier_id'] = forms.CharField(widget=forms.Select(attrs={'onchange': "get_supplier_details()"}), required=True)

        # choice = {k: v for k, v in SupplierMasterModel.objects.filter(status=1).order_by('id').values_list('id', 'supplier_name')}
        # supplier_list = list(choice.items())
        # self.fields['supplier_id'] = forms.ChoiceField(choice, widget = forms.Select(attrs = {'class':'form-control-input','onchange' : "myFunction();"}),choices=[('All', 'ALL')] + supplier_list,required=True)
        # print(supplier_list)
        
        # supplier_id = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control-input'}),
        #                                 choices=[('', 'Please select')] + supplier_list, required=False)
        
        # self.fields['supplier_id']= forms.ChoiceField(widget = forms.Select(attrs = {'onchange' : "get_supplier_details();"}))
        self.fields['supplier_id'] = forms.ModelChoiceField(queryset=SupplierMasterModel.objects.filter(status=1).order_by('id'), widget=forms.Select(attrs={"onChange":'getSupplier_data()'}))

        # self.fields['item_id'] = forms.ModelChoiceField(queryset=ItemMasterModel.objects.filter(status=1).order_by('id'), widget=forms.Select(attrs={"onChange":'getItems_data()'}))
        # self.fields['rate'].required = True 
         # self.fields['qty'].required = True
        # self.fields['total'].required = True

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
        # self.fields['qty'] = forms.CharField(widget=forms.TextInput(attrs={'onchange': "calculate()",'onkeyup': "calculate()",'onkeypress': "isNumber(event)"}), required=True)
        self.fields['qty'].required=True
        self.fields['total'].required = True

    class Meta:
        model = Purchase_DetailsModel
        fields = ['rate','qty','total']

# class purchaseTempForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(purchaseTempForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control-input'
        
#         self.fields['item_id'] = forms.ModelChoiceField(queryset=ItemMasterModel.objects.filter(status=1).order_by('id'), widget=forms.Select(attrs={"onChange":'getItems_data()'}))
#         self.fields['rate'].required=True
#         # self.fields['qty'] = forms.CharField(widget=forms.TextInput(attrs={'onchange': "calculate()",'onkeyup': "calculate()",'onkeypress': "isNumber(event)"}), required=True)
#         self.fields['qty'].required=True
#         self.fields['total'].required = True

#     class Meta:
#         model = Purchase_tempModel
#         fields = ['rate','qty','total']
        
        

