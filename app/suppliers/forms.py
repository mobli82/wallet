from django import forms

from .models import GazSupplierModel

class GazSupplierForm(forms.ModelForm):
    class Meta:
        model = GazSupplierModel
        fields = ['name', 
                  'vat', 
                  'conversion_rate', 
                  'distribution_fee', 
                  'gaz_fuel',
                  'subscription_fee',
                  'distribution_fee_constant',
        ]