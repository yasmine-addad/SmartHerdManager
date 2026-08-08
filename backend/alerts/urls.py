from django.urls import path

from .views import (
    AlerteListView,
    MarquerCommeLueView,
    SupprimerAlerteView,
)

urlpatterns = [
    path('', AlerteListView.as_view()),
    path('<int:pk>/lire/', MarquerCommeLueView.as_view()),
    path('<int:pk>/', SupprimerAlerteView.as_view()),
]