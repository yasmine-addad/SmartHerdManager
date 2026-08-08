from django.db import models
from animals.models import Animal


class DossierMedical(models.Model):

    animal = models.OneToOneField(
        Animal,
        on_delete=models.CASCADE,
        related_name="dossier_medical"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return f"Dossier médical - {self.animal.numero_identification}"


class Vaccination(models.Model):

    dossier_medical = models.ForeignKey(
        DossierMedical,
        on_delete=models.CASCADE,
        related_name="vaccinations"
    )

    type_vaccin = models.CharField(
        max_length=100
    )

    date_vaccination = models.DateField()

    date_rappel = models.DateField(
        null=True,
        blank=True
    )


    def __str__(self):
        return self.type_vaccin

class Maladie(models.Model):

    STATUT_CHOICES = (
        ("ACTIVE", "Active"),
        ("GUERIE", "Guérie"),
        ("CHRONIQUE", "Chronique"),
    )


    dossier_medical = models.ForeignKey(
        DossierMedical,
        on_delete=models.CASCADE,
        related_name="maladies"
    )

    nom = models.CharField(
        max_length=100
    )

    date_diagnostic = models.DateField()

    description = models.TextField(
        blank=True
    )

    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default="ACTIVE"
    )


    def __str__(self):
        return self.nom

class Traitement(models.Model):

    STATUT_CHOICES = (
        ("EN_COURS", "En cours"),
        ("TERMINE", "Terminé"),
        ("ARRETE", "Arrêté"),
    )


    dossier_medical = models.ForeignKey(
        DossierMedical,
        on_delete=models.CASCADE,
        related_name="traitements"
    )


    nom = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    date_debut = models.DateField()

    date_fin = models.DateField(
        null=True,
        blank=True
    )

    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default="EN_COURS"
    )


    def __str__(self):
        return self.nom

class VisiteVeterinaire(models.Model):

    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name="visites_veterinaires"
    )


    date = models.DateField()

    motif = models.CharField(
        max_length=200
    )

    veterinaire = models.CharField(
        max_length=100
    )

    observations = models.TextField(
        blank=True
    )


    def __str__(self):
        return f"Visite {self.animal.numero_identification}"
