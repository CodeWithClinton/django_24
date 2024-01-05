from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("index")
        
    context = {"form":form}
    return render(request, "core/signup.html", context)


def signin(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        
        else:
            messages.warning(request, "Invalid credentials")
            return redirect("signin")
        
    context = {}
    return render(request, "core/login.html", context)

def signout(request):
    logout(request)
    return redirect("index")