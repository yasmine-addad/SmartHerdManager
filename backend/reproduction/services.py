from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404

from animals.models import Animal
from .models import Reproduction, Naissance



def creer_reproduction(mere, date_insemination):
    
    return Reproduction.objects.create(
        mere=mere,
        date_insemination=date_insemination
    )


def liste_reproductions():
   
    return (
        Reproduction.objects
        .select_related("mere")
        .all()
    )


def get_reproduction(reproduction_id):
    
    return get_object_or_404(
        Reproduction,
        pk=reproduction_id
    )


def modifier_reproduction(
    reproduction,
    date_insemination=None,
    date_misebas_reelle=None
):
    

    if date_insemination is not None:
        reproduction.date_insemination = date_insemination

    if date_misebas_reelle is not None:
        reproduction.date_misebas_reelle = date_misebas_reelle

    reproduction.save()

    return reproduction


def supprimer_reproduction(reproduction):
   
    reproduction.delete()




@transaction.atomic
def enregistrer_naissance(
    reproduction,
    animal_enfant,
    date_naissance
):

    naissance = Naissance.objects.create(
        reproduction=reproduction,
        animal_enfant=animal_enfant,
        date_naissance=date_naissance
    )

    if reproduction.date_misebas_reelle is None:
        reproduction.date_misebas_reelle = date_naissance
        reproduction.save(update_fields=["date_misebas_reelle"])

    return naissance


def naissances_par_mere(mere):
    

    return (
        Naissance.objects
        .select_related(
            "animal_enfant",
            "reproduction",
            "reproduction__mere"
        )
        .filter(reproduction__mere=mere)
    )




def historique_reproduction(mere):
    

    return (
        Reproduction.objects
        .select_related("mere")
        .prefetch_related("naissances")
        .filter(mere=mere)
        .order_by("-date_insemination")
    )




def rechercher_reproduction(recherche):
    

    return (
        Reproduction.objects
        .select_related("mere")
        .filter(
            Q(mere__numero_identification__icontains=recherche)
            |
            Q(mere__race__icontains=recherche)
            |
            Q(mere__espece__icontains=recherche)
        )
        .distinct()
    )