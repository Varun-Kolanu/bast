from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .forms import AuctionForm
from product.models import Product

# Create your views here.
class AuctionView(View):

    def get(self, request, pk):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        form = AuctionForm()
        return render(request, 'bid/index.html', {'form': form, 'pk': pk})
    
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        form = AuctionForm(request.POST)
        auction = form.save(commit=False)
        auction.product = Product.objects.get(id=pk)
        auction.save()
        return redirect(reverse('main:home'))
