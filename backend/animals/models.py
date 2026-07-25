from django.db import models
from users.models import User
class Animal(models.Model):

    SEX_CHOICES=[
        ('M','Mâle'),
        ('F','Femelle'),
    ]

    STATUT_CHOICES=[
        ('ACTIF','Actif'),
        ('VENDU','Vendu'),
        ('DECEDE','Décédé'),
        ('MALADE','Malade'),
    ]

    numero_identification = models.CharField(
        max_length=50,
        unique=True
    )

    espece = models.CharField(
        max_length=100
    )

    race = models.CharField(
        max_length=100
    )

    sexe = models.CharField(
        max_length=1,
        choices=SEX_CHOICES
    )

    date_naissance = models.DateField()

    poids = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='ACTIF'
    )

    photo = models.ImageField(
        upload_to='animals/',
        blank=True,
        null=True
    )

    proprietaire = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='animals'
    )

    is_deleted = models.BooleanField(
    default=False
    )

    def __str__(self):
        return self.numero_identification + " - " + self.espece