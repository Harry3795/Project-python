from django import forms
from items.models import *
from django.db.models import Subquery


class itemsMasterForm(forms.ModelForm):
    
    def clean_item_name(self):
        data = self.cleaned_data['item_name']
        if len(data) < 4 :
            raise forms.ValidationError(' dfghjkl;dfghjk')

        return data
    class Meta:
        model = ItemMasterModel
        fields = ['brand_name','item_name','rate']
        labels = {
            'brand_name': "Brand Name",
            'item_name': "Item Name",
            'rate': "Rate",
        }
        error_messages = {
            # 'item_name': {
            #     'required': 'Please Enter Item Name',
            # },
            'brand_name': {
                'required': 'You must Select Choice',
            },
            'rate': {
                'required': 'Please Enter Rate',
            },
        }
    