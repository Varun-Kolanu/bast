from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'status', 'place', 'bought_date']
        widgets = {
            'bought_date': forms.DateInput(attrs={'type': 'date'}),
        }
