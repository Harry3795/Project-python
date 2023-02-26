from django import forms
from items.models import *
from django.db.models import Subquery


class itemsMasterForm(forms.ModelForm):
    brand_name = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control-input'}),
                        choices=[('', 'Please select'),('Realme','Realme'), ('Apple', 'Apple'), ('Lenovo', 'Lenovo')], required=True)

    def __init__(self, *args, **kwargs):
        super(itemsMasterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control-input'

        self.fields['item_name'].required = True
        self.fields['rate'].required = True

    class Meta:
        model = ItemMasterModel
        fields = ['brand_name','item_name','rate']
        labels = {
            'brand_name': "Brand Name",
            'item_name': "Item Name",
            'rate': "Rate",
        }
        error_messages = {
            'item_name': {
                'required': 'Please Enter Item Name',
            },
            'brand_name': {
                'required': 'You must Select Choice',
            },
            'rate': {
                'required': 'Please Enter Rate',
            },
        }