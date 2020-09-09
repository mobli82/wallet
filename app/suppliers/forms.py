from django import forms

from .models import GazSupplier

class GazSupplierForm(forms.ModelForm):
    class Meta:
        model = GazSupplier
        fields = ['name', 
                  'vat', 
                  'conversion_rate', 
                  'distribution_fee', 
                  'gaz_fuel',
                  'subscription_fee',
                  'distribution_fee_constant',
        ]