from django.db import models
from django.utils import timezone

class Tache(models.Model):
    STATUS_CHOICES = [
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
        ('en_attente', 'En attente'),
    ]

    titre = models.CharField(max_length=100, verbose_name="Titre de la tâche")
    description = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    date_echeance = models.DateTimeField(blank=True, null=True, verbose_name="Date d'échéance")
    statut = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='en_attente',
        verbose_name="Statut"
    )
    priorite = models.PositiveIntegerField(default=1, help_text="Priorité (1-5)")

    def __str__(self):
        return f"{self.titre} - {self.get_statut_display()}"

    class Meta:
        verbose_name = "Tâche"
        verbose_name_plural = "Tâches"