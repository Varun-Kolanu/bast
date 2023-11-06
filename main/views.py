import math
from django.shortcuts import render, redirect
from django.views import View
from product.models import Product, Category
from django.urls import reverse

# Create your views here.
class HomeView(View):
    def get(self, request):
        return redirect(reverse('main:category', args=('ALL',)))


class CategoryView(View):
    def get(self, request, category):
        if category == 'ALL':
            direct_sellings = Product.objects.filter(status='DIRSELL')
        else:
            direct_sellings = Product.objects.filter(status='DIRSELL', category=category)
        categories = Category.get_choices()
        context = {
            'direct_sellings': direct_sellings,
            'categories': categories,
            'present_category': category
        }
        return render(request, 'main/home.html', context)
