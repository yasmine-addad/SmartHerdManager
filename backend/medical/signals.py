from django.db.models.signals import post_save
from django.dispatch import receiver

from animals.models import Animal
from .models import DossierMedical


@receiver(post_save, sender=Animal)
def creer_dossier_medical_automatique(sender, instance, created, **kwargs):

    if created:

        DossierMedical.objects.create(
            animal=instance
        )