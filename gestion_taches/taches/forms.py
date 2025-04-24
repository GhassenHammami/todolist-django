from django import forms
from .models import Tache  # Import the Tache model instead of Contact

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['titre', 'description', 'date_echeance', 'statut', 'priorite']
        labels = {
            'titre': 'Titre de la tâche',
            'date_echeance': 'Date limite',
            'statut': 'Statut',
            'priorite': 'Priorité (1-5)',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'date_echeance': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }