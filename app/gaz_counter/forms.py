from django import forms
from .models import GazCounterModel

class GazCounterForm(forms.ModelForm):
    class Meta:
        model = GazCounterModel
        fields = ['value']