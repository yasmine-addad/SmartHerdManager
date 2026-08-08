from django.db import models
from django.conf import settings
from animals.models import Animal


class Alerte(models.Model):

    TYPE_CHOICES = [
        ('VACCIN', 'Vaccination'),
        ('MISE_BAS', 'Mise-bas'),
        ('VISITE', 'Visite vétérinaire'),
    ]

    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='alertes'
    )

    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name='alertes'
    )

    type_alerte = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    titre = models.CharField(max_length=255)

    message = models.TextField()

    date_alerte = models.DateField()

    STATUT_CHOICES = [
    ('ACTIVE', 'Active'),
    ('TRAITEE', 'Traitée'),
    ]

    statut = models.CharField(
    max_length=10,
    choices=STATUT_CHOICES,
    default='ACTIVE'
    )

    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['statut', '-date_alerte']

    def __str__(self):
        return f"{self.titre} - {self.animal.numero_identification}"