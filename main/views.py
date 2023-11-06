import math
from django.shortcuts import render
from django.views import View
from product.models import Product
from django.http import HttpResponse

# Create your views here.
class HomeView(View):
    def get(self, request):
        direct_sellings = Product.objects.filter(status='DIRSELL')
        auctions = Product.objects.filter(status='AUCTION')
        context = {
            'direct_sellings': direct_sellings,
            'auctions': auctions,
            'dirsell_length': range(math.ceil(len(direct_sellings)/3)),
            'auctions_length': range(math.ceil(len(auctions)/3))
        }
        return render(request, 'main/home.html', context)
        # return HttpResponse("Hi", status=200)
