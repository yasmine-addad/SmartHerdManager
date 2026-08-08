from .models import Alerte


def creer_alerte(
    utilisateur,
    animal,
    type_alerte,
    titre,
    message,
    date_alerte
):

    return Alerte.objects.create(
        utilisateur=utilisateur,
        animal=animal,
        type_alerte=type_alerte,
        titre=titre,
        message=message,
        date_alerte=date_alerte
    )