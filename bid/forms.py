from django import forms
from .models import AuctionItem, Bid

class AuctionForm(forms.ModelForm):
    class Meta:
        model = AuctionItem
        fields = ['starting_price', 'end_time']

        widgets = {
        'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    }


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount',]
