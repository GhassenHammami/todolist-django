from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Tache, UserProfile
from .forms import TacheForm, UserRegistrationForm, UserLoginForm, UserProfileForm

def landing_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'taches/landing.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Compte créé avec succès!')
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationForm()
    return render(request, 'taches/register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Connexion réussie!')
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserLoginForm()
    return render(request, 'taches/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Déconnexion réussie!')
    return redirect('landing_page')

@login_required
def dashboard(request):
    user_taches = Tache.objects.filter(user=request.user).order_by('-date_creation')
    total_taches = user_taches.count()
    termine_taches = user_taches.filter(statut='termine').count()
    en_cours_taches = user_taches.filter(statut='en_cours').count()
    en_attente_taches = user_taches.filter(statut='en_attente').count()
    
    context = {
        'taches': user_taches,
        'total_taches': total_taches,
        'termine_taches': termine_taches,
        'en_cours_taches': en_cours_taches,
        'en_attente_taches': en_attente_taches,
    }
    return render(request, 'taches/dashboard.html', context)

@login_required
def ajouter_tache(request):
    if request.method == "POST":
        form = TacheForm(request.POST)
        if form.is_valid():
            tache = form.save(commit=False)
            tache.user = request.user
            tache.save()
            messages.success(request, 'Tâche ajoutée avec succès!')
            return redirect('dashboard')
    else:
        form = TacheForm()
    return render(request, 'taches/ajouter.html', {'form': form})

@login_required
def modifier_tache(request, pk):
    tache = get_object_or_404(Tache, pk=pk, user=request.user)
    if request.method == "POST":
        form = TacheForm(request.POST, instance=tache)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tâche modifiée avec succès!')
            return redirect('dashboard')
    else:
        form = TacheForm(instance=tache)
    return render(request, 'taches/modifier.html', {'form': form, 'tache': tache})

@login_required
def supprimer_tache(request, pk):
    tache = get_object_or_404(Tache, pk=pk, user=request.user)
    if request.method == "POST":
        tache.delete()
        messages.success(request, 'Tâche supprimée avec succès!')
        return redirect('dashboard')
    return render(request, 'taches/supprimer.html', {'tache': tache})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil mis à jour avec succès!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'taches/profile.html', {'form': form})