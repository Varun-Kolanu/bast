from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .forms import DirectSellForm
from product.models import Product

# Create your views here.
class DirectSellView(View):

    def get(self, request, pk):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        form = DirectSellForm()
        return render(request, 'direct_sell/index.html', {'form': form, 'pk': pk})
    
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        form = DirectSellForm(request.POST)
        dir_sell = form.save(commit=False)
        dir_sell.product = Product.objects.get(id=pk)
        dir_sell.save()
        return redirect(reverse('main:home'))
