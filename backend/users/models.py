from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):

    GENDER_CHOICES = [
        ('M','Homme'),
        ('F','Femme'),
    ]
    #id,nom,prenom,email,adresse,mot de passe, date création
    genre = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)

    telephone = models.CharField(max_length=20, null=True, blank=True)

    photo_profil = models.ImageField(upload_to='profiles/', null=True, blank=True)

    statut_compte = models.BooleanField(default=True)

    adresse = models.CharField(max_length=255 ,null=True, blank=True)

    email = models.EmailField(unique=True, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
       return self.email

class Licence(models.Model):
    
    TYPE_CHOICES = [
        ('ESSAI', 'Essai'),
        ('STANDARD', 'Standard'),
        ('PREMIUM', 'Premium'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    date_debut = models.DateField()

    date_expiration = models.DateField()

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="licence"
    )

    @property
    def statut(self):
        if self.date_expiration >= timezone.now().date():
            return "ACTIVE"
        return "EXPIREE"

    def __str__(self):
        return self.type


class Action(models.Model):

    TYPE_CHOICES = [
        ('SANTE', 'Santé'),
        ('VENTE', 'Vente'),
        ('NAISSANCE', 'Naissance'),
        ('AUTRE', 'Autre'),
    ]

    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


class Historique(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="historique"
    )



    def __str__(self):
        return f"Historique de {self.user.first_name}"
    

class HistoriqueAction(models.Model):

    TYPE_CHOICES = [
        ('LOGIN', 'Connexion'),
        ('LOGOUT', 'Déconnexion'),
        ('PROFILE_UPDATE', 'Modification du profil'),

        ('ANIMAL_CREATE', 'Ajout d’un animal'),
        ('ANIMAL_UPDATE', 'Modification d’un animal'),
        ('ANIMAL_DELETE', 'Suppression d’un animal'),
        ('STATUS_CHANGE', 'Changement de statut'),
        ('WEIGHT_UPDATE', 'Modification du poids'),
        ('PHOTO_UPDATE', 'Modification de la photo'),
    ]

    animal = models.ForeignKey(
    "animals.Animal",
    on_delete=models.SET_NULL,
    related_name="historique_actions",
    null=True,
    blank=True
    )

    historique = models.ForeignKey(
        Historique,
        on_delete=models.CASCADE,
        related_name="actions"
    )

    type_action = models.CharField(
        max_length=30,
        choices=TYPE_CHOICES
    )

    details = models.TextField(blank=True)

    date_action = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type_action
    
