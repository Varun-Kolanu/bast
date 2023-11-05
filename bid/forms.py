from django import forms
from .models import AuctionItem

class AuctionForm(forms.ModelForm):
    class Meta:
        model = AuctionItem
        fields = ['starting_price', 'end_time']

        widgets = {
        'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    }
