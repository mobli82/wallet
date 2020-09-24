from django import forms

from .models import GazSupplierModel, PowerSupplierModel

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

class PowerSupplierForm(forms.ModelForm):
    class Meta:
        model = PowerSupplierModel
        fields = ['name', 
                  'vat', 
                  'energy_fee', 
                  'subscription_fee', 
                  'network_fee_constant',
                  'network_fee_24_7',
                  'quality_fee',
                  'oze_fee',
                  'cogeneration_fee',
                  'transitional_fee',
        ]