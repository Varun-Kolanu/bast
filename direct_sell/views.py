from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .forms import DirectSellForm
from product.models import Product
from bid.models import Bid
from .models import DirectsellProduct
from product.forms import ProductEditForm

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


class DirectSellEditView(View):

    def get(self,request, pk):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        product = Product.objects.get(id=pk)
        direct_sell = DirectsellProduct.objects.get(product=product)
        product_edit_form = ProductEditForm(instance=product)
        direct_sell_form = DirectSellForm(instance=direct_sell)
        context = {
            'product_edit_form': product_edit_form,
            'direct_sell_form': direct_sell_form,
            'pk': pk
        }
        return render(request, 'direct_sell/edit_form.html', context)
    
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        
        product = Product.objects.get(id=pk)
        direct_sell = DirectsellProduct.objects.get(product=product)
        product_edit_form = ProductEditForm(request.POST, request.FILES, instance=product)
        direct_sell_form = DirectSellForm(request.POST, instance=direct_sell)
        if direct_sell_form.is_valid() and product_edit_form.is_valid():
            direct_sell_form.save()
            product_edit_form.save()
            return redirect(reverse('Authentication:profile'))
        else:
            product_edit_form = ProductEditForm(instance=product)
            return render(request, 'direct_sell/edit_form.html', {
                'product_edit_form': product_edit_form,
                'direct_sell_form': direct_sell_form,
                'pk': pk
            })
