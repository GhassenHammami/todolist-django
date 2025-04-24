from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('ajouter/', views.ajouter_tache, name='ajouter_tache'),
    path('modifier/<int:pk>/', views.modifier_tache, name='modifier_tache'),
    path('supprimer/<int:pk>/', views.supprimer_tache, name='supprimer_tache'),
]