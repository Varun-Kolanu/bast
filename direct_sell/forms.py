from django import forms
from .models import DirectsellProduct

class DirectSellForm(forms.ModelForm):
    class Meta:
        model = DirectsellProduct
        fields = ['price']
