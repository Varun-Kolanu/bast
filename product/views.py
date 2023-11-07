from django.shortcuts import render, redirect
from django.views import View
from .forms import ProductForm
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Product, Status
from direct_sell.forms import DirectSellForm
from bid.forms import AuctionForm

# Create your views here

# @method_decorator(login_required(login_url=reverse('main:home')), name='dispatch')
class ProductCreateView(View):

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('Authentication:login'))
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            status = form.cleaned_data.get('status')
            if status == 'DIRSELL':
                return redirect(reverse('direct_sell:direct_sell', args=(product.id,)))
            if status == 'AUCTION':
                return redirect(reverse('bid:bid', args=(product.id,)))
            return redirect(reverse('main:home'))
        else:
            return render(request, 'product/index.html', {'form': form})
    

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('Authentication:login'))
        form = ProductForm()
        return render(request, 'product/index.html', {'form': form})


class ProductView(View):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'product/view.html', {'product': product})


class ProductDeleteView(View):

    def get(self, request,pk):
        Product.objects.get(pk=pk).delete()
        return redirect(reverse('main:home'))


class ProductChangeStatusView(View):

    def get(self, request,pk):
        product = Product.objects.get(pk=pk)
        if product.status == 'DIRSELL':
            form = AuctionForm()
            return render(request, 'bid/index.html', {'form': form, 'pk': pk, 'moving': True})
        else:
            form = DirectSellForm()
            return render(request, 'direct_sell/index.html', {'form': form, 'pk': pk, 'moving': True})

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        if product.status == 'DIRSELL':
            form = AuctionForm(request.POST)
            if form.is_valid():
                product.directsellproduct.delete()
                product.status = 'AUCTION'
                product.save()
                auction = form.save(commit=False)
                auction.product = product
                auction.save()
                return redirect(reverse('main:home'))
            else:
                return render(request, 'bid/index.html', {'form': form, 'pk': pk})
        else:
            form = DirectSellForm(request.POST)
            if form.is_valid():
                product.auctionitem.delete()
                product.status = 'DIRSELL'
                product.save()
                dir_sell = form.save(commit=False)
                dir_sell.product = Product.objects.get(pk=pk)
                dir_sell.save()
                return redirect(reverse('main:home'))
            else:
                return render(request, 'direct_sell/index.html', {'form': form, 'pk': pk})



