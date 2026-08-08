from django.contrib import admin

from .models import (
    DossierMedical,
    Vaccination,
    Maladie,
    Traitement,
    VisiteVeterinaire
)


@admin.register(DossierMedical)
class DossierMedicalAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "animal",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "animal__numero_identification",
    )


@admin.register(Vaccination)
class VaccinationAdmin(admin.ModelAdmin):

    list_display = (
        "type_vaccin",
        "dossier_medical",
        "date_vaccination",
        "date_rappel",
    )

    list_filter = (
        "date_vaccination",
    )

    search_fields = (
        "type_vaccin",
        "dossier_medical__animal__numero_identification",
    )


@admin.register(Maladie)
class MaladieAdmin(admin.ModelAdmin):

    list_display = (
        "nom",
        "dossier_medical",
        "statut",
        "date_diagnostic",
    )

    list_filter = (
        "statut",
    )

    search_fields = (
        "nom",
        "dossier_medical__animal__numero_identification",
    )


@admin.register(Traitement)
class TraitementAdmin(admin.ModelAdmin):

    list_display = (
        "nom",
        "dossier_medical",
        "statut",
        "date_debut",
        "date_fin",
    )

    list_filter = (
        "statut",
    )

    search_fields = (
        "nom",
        "dossier_medical__animal__numero_identification",
    )


@admin.register(VisiteVeterinaire)
class VisiteVeterinaireAdmin(admin.ModelAdmin):

    list_display = (
        "animal",
        "date",
        "motif",
        "veterinaire",
    )

    list_filter = (
        "date",
    )

    search_fields = (
        "animal__numero_identification",
        "veterinaire",
    )