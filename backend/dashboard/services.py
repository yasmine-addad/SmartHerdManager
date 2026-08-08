from django.db.models import Count
from django.utils import timezone

from animals.models import Animal
from medical.models import Maladie, Traitement
from reproduction.models import Reproduction, Naissance


def get_dashboard_statistics():

    aujourd_hui = timezone.now().date()

    debut_mois = aujourd_hui.replace(day=1)

    statistiques = {

        "animaux_par_espece": list(
            Animal.objects
            .values("espece")
            .annotate(total=Count("id"))
        ),

         "femelles_gestantes": Reproduction.objects.filter(
            date_misebas_reelle__isnull=True,
            date_misebas_prevue__gte=aujourd_hui
        ).count(),

        "animaux_malades": Maladie.objects.filter(
            statut="ACTIVE"
        ).count(),

        "animaux_en_traitement": Traitement.objects.filter(
            statut="EN_COURS"
        ).count(),

        "naissances_mois": Naissance.objects.filter(
            date_naissance__gte=debut_mois
        ).count(),
    }

    return statistiques