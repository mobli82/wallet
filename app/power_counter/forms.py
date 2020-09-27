from django import forms
from .models import PowerCounterModel

class PowerCounterForm(forms.ModelForm):
    class Meta:
        model = PowerCounterModel
        fields = ['value', 'monthly_usage']