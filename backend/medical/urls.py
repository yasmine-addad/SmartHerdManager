from django.urls import path

from .views import (
    DossierMedicalDetailView,
    VaccinationView,
    MaladieView,
    TraitementView,
    VisiteVeterinaireView,
)


urlpatterns = [

    # ==========================
    # Dossier médical
    # ==========================

    path(
        "animals/<int:animal_id>/dossier/",
        DossierMedicalDetailView.as_view(),
        name="dossier-medical-detail"
    ),


    # ==========================
    # Vaccinations
    # ==========================

    path(
        "animals/<int:animal_id>/vaccinations/",
        VaccinationView.as_view(),
        name="vaccination-list-create"
    ),


    # ==========================
    # Maladies
    # ==========================

    path(
        "animals/<int:animal_id>/maladies/",
        MaladieView.as_view(),
        name="maladie-list-create"
    ),


    # ==========================
    # Traitements
    # ==========================

    path(
        "animals/<int:animal_id>/traitements/",
        TraitementView.as_view(),
        name="traitement-list-create"
    ),


    # ==========================
    # Visites vétérinaires
    # ==========================

    path(
        "animals/<int:animal_id>/visites/",
        VisiteVeterinaireView.as_view(),
        name="visite-list-create"
    ),

]