from django.urls import path

from .views import (
    ReproductionListCreateView,
    ReproductionDetailView,
    NaissanceListCreateView,
    NaissancesParMereView,
    HistoriqueReproductionView,
    RechercheReproductionView,
)

urlpatterns = [
    
    path(
        "reproductions/",
        ReproductionListCreateView.as_view(),
        name="reproduction-list-create",
    ),

    path(
        "reproductions/<int:pk>/",
        ReproductionDetailView.as_view(),
        name="reproduction-detail",
    ),

   
    path(
        "naissances/",
        NaissanceListCreateView.as_view(),
        name="naissance-list-create",
    ),

    path(
        "meres/<int:mere_id>/naissances/",
        NaissancesParMereView.as_view(),
        name="naissances-par-mere",
    ),

    
    path(
        "meres/<int:mere_id>/historique/",
        HistoriqueReproductionView.as_view(),
        name="historique-reproduction",
    ),

   
    path(
        "recherche/",
        RechercheReproductionView.as_view(),
        name="recherche-reproduction",
    ),
]