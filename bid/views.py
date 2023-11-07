from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .forms import AuctionForm
from product.models import Product, Category
from .models import AuctionItem
from product.forms import ProductEditForm

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
        if form.is_valid():
            auction = form.save(commit=False)
            auction.product = Product.objects.get(pk=pk)
            auction.save()
            return redirect(reverse('main:home'))
        else:
            return render(request, 'bid/index.html', {'form': form, 'pk': pk})



class AuctionEditView(View):

    def get(self,request, pk):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        product = Product.objects.get(pk=pk)
        auction_item = AuctionItem.objects.get(product=product)
        product_edit_form = ProductEditForm(instance=product)
        auction_form = AuctionForm(instance=auction_item)
        context = {
            'product_edit_form': product_edit_form,
            'auction_form': auction_form,
            'pk': pk
        }
        return render(request, 'bid/edit_form.html', context)
    
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        
        product = Product.objects.get(pk=pk)
        auction_item = AuctionItem.objects.get(product=product)
        product_edit_form = ProductEditForm(request.POST, request.FILES, instance=product)
        auction_form = AuctionForm(request.POST, instance=auction_item)
        if auction_form.is_valid() and product_edit_form.is_valid():
            auction_form.save()
            product_edit_form.save()
            return redirect(reverse('Authentication:profile'))
        else:
            product_edit_form = ProductEditForm(instance=product)
            return render(request, 'direct_sell/edit_form.html', {
                'product_edit_form': product_edit_form,
                'auction_form': auction_form,
                'pk': pk
            })


class ShowAuctionsView(View):

    def get(self, request):
        return redirect(reverse('bid:category', args=('ALL',)))


class MyAuctions(View):

    def get(self, request):
        auctions = Product.objects.filter(status='AUCTION', owner=request.user)
        context = {
            'auctions': auctions,
        }
        return render(request, 'bid/my_auctions.html', context)


class CategoryView(View):

    def get(self, request, category):
        if category == 'ALL':
            auctions = Product.objects.filter(status='AUCTION')
        else:
            auctions = Product.objects.filter(status='AUCTION', category=category)
        categories = Category.get_choices()
        context = {
            'auctions': auctions,
            'categories': categories,
            'present_category': category
        }
        return render(request, 'bid/auctions.html', context)
