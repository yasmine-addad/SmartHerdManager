from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from animals.models import Animal
from .models import Reproduction
from .serializers import (
    ReproductionSerializer,
    NaissanceSerializer
)
from .services import (
    creer_reproduction,
    liste_reproductions,
    get_reproduction,
    modifier_reproduction,
    supprimer_reproduction,
    enregistrer_naissance,
    naissances_par_mere,
    historique_reproduction,
    rechercher_reproduction
)


class ReproductionListCreateView(APIView):

    def get(self, request):
        reproductions = liste_reproductions()
        serializer = ReproductionSerializer(reproductions, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = ReproductionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mere = get_object_or_404(
            Animal,
            pk=serializer.validated_data["mere"].id
        )

        reproduction = creer_reproduction(
            mere=mere,
            date_insemination=serializer.validated_data["date_insemination"]
        )

        return Response(
            ReproductionSerializer(reproduction).data,
            status=status.HTTP_201_CREATED
        )



class ReproductionDetailView(APIView):

    def get(self, request, pk):

        reproduction = get_reproduction(pk)

        serializer = ReproductionSerializer(reproduction)

        return Response(serializer.data)

    def put(self, request, pk):

        reproduction = get_reproduction(pk)

        serializer = ReproductionSerializer(
            reproduction,
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        reproduction = modifier_reproduction(
            reproduction=reproduction,
            date_insemination=serializer.validated_data.get(
                "date_insemination"
            ),
            date_misebas_reelle=serializer.validated_data.get(
                "date_misebas_reelle"
            )
        )

        return Response(
            ReproductionSerializer(reproduction).data
        )

    def delete(self, request, pk):

        reproduction = get_reproduction(pk)

        supprimer_reproduction(reproduction)

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )




class NaissanceListCreateView(APIView):

    def post(self, request):

        serializer = NaissanceSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        reproduction = get_object_or_404(
            Reproduction,
            pk=serializer.validated_data["reproduction"].id
        )

        animal = get_object_or_404(
            Animal,
            pk=serializer.validated_data["animal_enfant"].id
        )

        naissance = enregistrer_naissance(
            reproduction=reproduction,
            animal_enfant=animal,
            date_naissance=serializer.validated_data["date_naissance"]
        )

        return Response(
            NaissanceSerializer(naissance).data,
            status=status.HTTP_201_CREATED
        )




class NaissancesParMereView(APIView):

    def get(self, request, mere_id):

        mere = get_object_or_404(
            Animal,
            pk=mere_id
        )

        naissances = naissances_par_mere(mere)

        serializer = NaissanceSerializer(
            naissances,
            many=True
        )

        return Response(serializer.data)




class HistoriqueReproductionView(APIView):

    def get(self, request, mere_id):

        mere = get_object_or_404(
            Animal,
            pk=mere_id
        )

        historique = historique_reproduction(mere)

        serializer = ReproductionSerializer(
            historique,
            many=True
        )

        return Response(serializer.data)


class RechercheReproductionView(APIView):

    def get(self, request):

        recherche = request.query_params.get("q", "")

        reproductions = rechercher_reproduction(recherche)

        serializer = ReproductionSerializer(
            reproductions,
            many=True
        )

        return Response(serializer.data)