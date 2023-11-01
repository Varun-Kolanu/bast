from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.views import View
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
class RegisterView(View):
    """
    User registration view
    """

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'Authentication/register.html', context)
    

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('user')
            password = form.cleaned_data.get('pass')
            # user = authenticate(username=username, password=password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(reverse('home'))
        else:
            form = RegisterForm(request.POST)
            context = {
                'form': form
            }
            return render(request, 'Authentication/register.html', context)



class HomeView(View):
    def get(self, request):
        return HttpResponse("Registered Successfully")
