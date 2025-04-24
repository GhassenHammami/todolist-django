from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class Tache(models.Model):
    STATUS_CHOICES = [
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
        ('en_attente', 'En attente'),
    ]

    PRIORITY_CHOICES = [
        (1, 'Basse'),
        (2, 'Moyenne-Basse'),
        (3, 'Moyenne'),
        (4, 'Moyenne-Haute'),
        (5, 'Haute'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taches')
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
    priorite = models.PositiveIntegerField(
        choices=PRIORITY_CHOICES,
        default=3,
        help_text="Priorité (1-5)"
    )
    tags = models.CharField(max_length=100, blank=True, help_text="Séparez les tags par des virgules")

    def __str__(self):
        return f"{self.titre} - {self.get_statut_display()}"

    class Meta:
        verbose_name = "Tâche"
        verbose_name_plural = "Tâches"
        ordering = ['-date_creation']