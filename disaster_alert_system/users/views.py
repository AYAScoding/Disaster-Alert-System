from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # The save method in the form now handles everything
            return redirect('users:home')
        else:
            # Add messages for specific errors if needed
            if 'username' in form.errors:
                messages.error(request, 'Username already exists.')
            if 'password2' in form.errors:
                messages.error(request, 'Passwords do not match.')
            # You can add more custom error handling for other fields as needed
    else:
        form = UserRegisterForm()

    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:home')
            else:
               messages.error(request, 'Invalid username or password')
        
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('users:login')
