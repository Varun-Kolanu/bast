from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .forms import AuctionForm, BidForm
from product.models import Product, Category
from .models import AuctionItem, Bid
from product.forms import ProductEditForm
from django.utils import timezone

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
        current_time = timezone.now()
        if category == 'ALL':
            auctions = Product.objects.filter(status='AUCTION', auctionitem__end_time__gte=current_time)
        else:
            auctions = Product.objects.filter(status='AUCTION', category=category, auctionitem__end_time__gte=current_time)
        categories = Category.get_choices()
        context = {
            'auctions': auctions,
            'categories': categories,
            'present_category': category
        }
        return render(request, 'bid/auctions.html', context)


class BidView(View):

    def get(self,request, pk):
        if not request.user.is_authenticated:
            return redirect(reverse('Authentication:login'))
        auctionitem = AuctionItem.objects.get(pk=pk)
        form = BidForm()
        context = {
            'auctionitem': auctionitem,
            'form': form
        }
        return render(request, 'bid/make_bid.html', context)
    

    def post(self,request,pk):
        if not request.user.is_authenticated:
            return redirect(reverse('Authentication:login'))
        form = BidForm(request.POST)
        auctionitem = AuctionItem.objects.get(pk=pk)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            existing_bid = Bid.objects.filter(bidder=request.user).first()
            auctionitem = AuctionItem.objects.get(pk=pk)
            if auctionitem.current_highest_bid and amount <= auctionitem.current_highest_bid:
                context = {
                    'auctionitem': auctionitem,
                    'form': form,
                    'error_message': 'Bid should be higher than current highest bid'
                }
                return render(request, 'bid/make_bid.html', context)
            elif amount <= auctionitem.starting_price:
                context = {
                    'auctionitem': auctionitem,
                    'form': form,
                    'error_message': 'Bid should be higher than Starting Price'
                }
                return render(request, 'bid/make_bid.html', context)
            auctionitem.current_highest_bid = amount
            auctionitem.highest_bidder = request.user
            auctionitem.save()
            if existing_bid is not None:
                existing_bid.amount = amount
                existing_bid.save()
            else:
                bid = form.save(commit=False)
                bid.bidder = request.user
                bid.auction_item = auctionitem
                bid.save()
            return redirect(reverse('product:product', args=(auctionitem.product.id,)))
        else:
            context = {
            'auctionitem': auctionitem,
            'form': form
            }
            return render(request, 'bid/make_bid.html', context)
