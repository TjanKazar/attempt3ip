from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import PrijavaForm
from .models import Prijavnica
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

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
            prijavnica = form.save(commit=False)
            prijavnica.user = request.user
            prijavnica.save()
            return redirect(reverse("home"))
    else:
        form = PrijavaForm()
    return render(request, "prijavnica.html", {"form": form})

@login_required
def user_prijavnice(request):
    user_prijavnice_list = Prijavnica.objects.filter(user=request.user)
    return render(request, 'user_prijavnice.html', {'prijavnice_list': user_prijavnice_list})

@login_required
def user_edit_prijavnica(request, pk):
    prijavnica = get_object_or_404(Prijavnica, pk=pk, user=request.user)
    if request.method == "POST":
        form = PrijavaForm(request.POST, instance=prijavnica)
        if form.is_valid():
            prijavnica = form.save(commit=False)
            prijavnica.valid = None  # Reset the validation status
            prijavnica.save()
            return redirect('user_prijavnice')
    else:
        form = PrijavaForm(instance=prijavnica)
    return render(request, 'user_edit_prijavnica.html', {'form': form})

@login_required
@csrf_exempt
def edit_prijavnica(request, prijavnica_id):
    prijavnica_instance = get_object_or_404(Prijavnica, pk=prijavnica_id)
    
    if request.method == "POST":
        # Get the value of 'komentar' from the form
        komentar = request.POST.get('komentar')
        valid = 'valid' in request.POST
        
        # Update the 'komentar' field of the instance
        prijavnica_instance.komentar = komentar
        prijavnica_instance.valid = valid
        
        # Save the instance
        prijavnica_instance.save()
        
        return redirect(reverse("home"))
    
    return render(request, "edit_prijavnica.html", {"prijavnica_instance": prijavnica_instance})
