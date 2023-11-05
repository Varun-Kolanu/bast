from django.shortcuts import render, redirect
from django.views import View
from .forms import ProductForm
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Product

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
            print(status == 'DIRSELL')
            if status == 'DIRSELL':
                return redirect(reverse('direct_sell:direct_sell', args=(product.id,)))
            if status == 'AUCTION':
                return redirect(reverse('bid:bid', args=(product.id,)))
            return redirect(reverse('main:home'))
        else:
            print(form)
            return render(request, 'product/index.html', {'form': form})
    

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('Authentication:login'))
        form = ProductForm()
        return render(request, 'product/index.html', {'form': form})


