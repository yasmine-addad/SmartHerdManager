from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Animal
from .serializers import AnimalSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .filters import AnimalFilter

from users.models import HistoriqueAction

from users.serializers import AnimalHistoriqueSerializer


class AnimalListCreateView(generics.ListCreateAPIView):

    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]

    filterset_class = AnimalFilter

    search_fields = [
        'numero_identification',
    ]


    def get_queryset(self):
        return Animal.objects.filter(
            proprietaire=self.request.user,
            is_deleted=False
        )

    def perform_create(self, serializer):
        animal = serializer.save(
        proprietaire=self.request.user
        )

        HistoriqueAction.objects.create(
            historique=self.request.user.historique,
            animal=animal,
            type_action="ANIMAL_CREATE",
            details=f"Ajout de l'animal {animal.numero_identification}"
        )

class AnimalDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Animal.objects.filter(
            proprietaire=self.request.user,
            is_deleted=False
        )
    
    def perform_update(self, serializer):
        animal = serializer.save()

        HistoriqueAction.objects.create(
            historique=self.request.user.historique,
            animal=animal,
            type_action="ANIMAL_UPDATE",
            details=f"Modification de l'animal {animal.numero_identification}"
        )

    def perform_destroy(self, instance):

         HistoriqueAction.objects.create(
            historique=self.request.user.historique,
            animal=instance,
            type_action="ANIMAL_DELETE",
            details=f"Suppression de l'animal {instance.numero_identification}"
        )

         instance.is_deleted=True
         instance.save()

class AnimalHistoryView(generics.ListAPIView):

    serializer_class = AnimalHistoriqueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        animal_id = self.kwargs["pk"]

        return HistoriqueAction.objects.filter(
            animal_id=animal_id,
            historique__user=self.request.user
        ).order_by("-date_action")