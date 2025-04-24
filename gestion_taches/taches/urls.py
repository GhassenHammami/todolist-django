from django.urls import path
from . import views

urlpatterns = [
    path('ajouter/', views.ajouter_tache, name='ajouter_tache'),
    path('liste/', views.liste_taches, name='liste_taches'),
]