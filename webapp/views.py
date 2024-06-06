from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import PrijavaForm
from .models import Prijavnica

@login_required
def home(request):
    if request.user.is_staff:
        return render(request, "home.html")
    else:
        return render(request, "user_home.html")

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, "login.html")

@login_required
def prijavnice(request):
    if request.user.is_staff:
        prijave = Prijavnica.objects.all()
        return render(request, "prijavnice.html", {"prijavnica_list": prijave})
    else:
        return redirect(reverse('home'))

@login_required
def prijavnica(request):
    if request.user.is_staff:
        return redirect(reverse('home'))
    
    if request.method == "POST":
        form = PrijavaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("home"))
    else:
        form = PrijavaForm()
    return render(request, "prijavnica.html", {"form": form})
