from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Alerte
from .serializers import AlerteSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AlerteListView(generics.ListAPIView):

    serializer_class = AlerteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Alerte.objects.filter(
            utilisateur=self.request.user
        )

class MarquerCommeLueView(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):

        alerte = Alerte.objects.get(
            pk=pk,
            utilisateur=request.user
        )

        alerte.statut = 'TRAITEE'
        alerte.save()

        return Response(
            {"message": "Alerte marquée comme lue"},
            status=status.HTTP_200_OK
        )

class SupprimerAlerteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Alerte.objects.filter(utilisateur=self.request.user)

    def destroy(self, request, *args, **kwargs):
        alerte = self.get_object()

        if alerte.statut == "ACTIVE":
            return Response(
                {
                    "detail": "Impossible de supprimer une alerte non traitée."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().destroy(request, *args, **kwargs)