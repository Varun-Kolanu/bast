import math
from django.shortcuts import render
from django.views import View
from product.models import Product
from django.http import HttpResponse

# Create your views here.
class HomeView(View):
    def get(self, request):
        direct_sellings = Product.objects.filter(status='DIRSELL')
        context = {
            'direct_sellings': direct_sellings,
        }
        return render(request, 'main/home.html', context)
