from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, AuthenticationForm
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
            return redirect(reverse('main:home'))
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'Authentication/register.html', context)
    

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(reverse('main:home'))
        else:
            form = RegisterForm(request.POST)
            context = {
                'form': form
            }
            return render(request, 'Authentication/register.html', context)



class LoginView(View):
    """
    User Login view
    """

    def get(self,request):
        if request.user.is_authenticated:
            return redirect(reverse('main:home'))
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'Authentication/login.html', context)


    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('main:home'))
        else:
            form = AuthenticationForm(request.POST)
            context = {
                'form': form,
                'error_message': 'Invalid username or password'
            }
            return render(request, 'Authentication/login.html', context)


class LogoutView(View):
    """
    Logout view
    """

    def get(self,request):
        logout(request)
        return redirect(reverse('Authentication:login'))



class ProfileView(View):
    
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect(reverse('Authentication:login'))
        context = {
            'user': request.user
        }
        return render(request, 'Authentication/profile.html', context)