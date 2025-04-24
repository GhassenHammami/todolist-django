from django.shortcuts import render, redirect
from .models import Tache
from .forms import TacheForm

def ajouter_tache(request):
    if request.method == "POST":
        form = TacheForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_taches')
    else:
        form = TacheForm()
    return render(request, 'taches/ajouter.html', {'form': form})

def liste_taches(request):
    taches = Tache.objects.all().order_by('-date_creation')
    return render(request, 'taches/liste.html', {'taches': taches})