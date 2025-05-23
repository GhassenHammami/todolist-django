# Generated by Django 5.2 on 2025-04-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100, verbose_name='Titre de la tâche')),
                ('description', models.TextField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('date_echeance', models.DateTimeField(blank=True, null=True, verbose_name="Date d'échéance")),
                ('statut', models.CharField(choices=[('en_cours', 'En cours'), ('termine', 'Terminé'), ('en_attente', 'En attente')], default='en_attente', max_length=20, verbose_name='Statut')),
                ('priorite', models.PositiveIntegerField(default=1, help_text='Priorité (1-5)')),
            ],
            options={
                'verbose_name': 'Tâche',
                'verbose_name_plural': 'Tâches',
            },
        ),
    ]
