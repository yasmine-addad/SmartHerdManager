from .models import (
    DossierMedical,
    Vaccination,
    Maladie,
    Traitement,
    VisiteVeterinaire
)

from users.models import Historique, HistoriqueAction

from rest_framework.exceptions import NotFound

from animals.models import Animal


def ajouter_historique(
        user,
        type_action,
        details="",
        animal=None
):

    historique, created = Historique.objects.get_or_create(
        user=user
    )

    HistoriqueAction.objects.create(
        historique=historique,
        animal=animal,
        type_action=type_action,
        details=details
    )


def creer_dossier_medical(animal):

    dossier = DossierMedical.objects.create(
        animal=animal
    )

    return dossier


def get_dossier_medical(animal_id):

    try:
        return DossierMedical.objects.prefetch_related(
            "vaccinations",
            "maladies",
            "traitements"
        ).get(
            animal_id=animal_id
        )

    except DossierMedical.DoesNotExist:

        raise NotFound(
            "Aucun dossier médical trouvé"
        )


def ajouter_vaccination(
        user,
        dossier,
        type_vaccin,
        date_vaccination,
        date_rappel=None
):

    vaccination = Vaccination.objects.create(
        dossier_medical=dossier,
        type_vaccin=type_vaccin,
        date_vaccination=date_vaccination,
        date_rappel=date_rappel
    )

    ajouter_historique(
        user=user,
        animal=dossier.animal,
        type_action="AJOUT_VACCINATION",
        details=f"Ajout du vaccin {type_vaccin} pour l'animal {dossier.animal.numero_identification}"
    )

    return vaccination


def ajouter_maladie(
        user,
        dossier,
        nom,
        date_diagnostic,
        description=""
):

    maladie = Maladie.objects.create(
        dossier_medical=dossier,
        nom=nom,
        date_diagnostic=date_diagnostic,
        description=description
    )

    ajouter_historique(
        user=user,
        animal=dossier.animal,
        type_action="AJOUT_MALADIE",
        details=f"Ajout de la maladie {nom} pour l'animal {dossier.animal.numero_identification}"
    )

    return maladie


def ajouter_traitement(
        user,
        dossier,
        nom,
        description,
        date_debut,
        date_fin=None
):

    traitement = Traitement.objects.create(
        dossier_medical=dossier,
        nom=nom,
        description=description,
        date_debut=date_debut,
        date_fin=date_fin
    )

    ajouter_historique(
        user=user,
        animal=dossier.animal,
        type_action="AJOUT_TRAITEMENT",
        details=f"Ajout du traitement {nom} pour l'animal {dossier.animal.numero_identification}"
    )

    return traitement


def ajouter_visite_veterinaire(
        user,
        animal,
        date,
        motif,
        veterinaire,
        observations=""
):

    visite = VisiteVeterinaire.objects.create(
        animal=animal,
        date=date,
        motif=motif,
        veterinaire=veterinaire,
        observations=observations
    )

    ajouter_historique(
        user=user,
        animal=animal,
        type_action="AJOUT_VISITE_VETERINAIRE",
        details=f"Nouvelle visite vétérinaire pour l'animal {animal.numero_identification}"
    )

    return visite

def get_user_animal(user, animal_id):
    try:
        return Animal.objects.get(
            id=animal_id,
            proprietaire=user
        )

    except Animal.DoesNotExist:
        raise NotFound("Animal introuvable")