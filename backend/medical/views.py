from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    DossierMedicalSerializer,
    VaccinationSerializer,
    MaladieSerializer,
    TraitementSerializer,
    VisiteVeterinaireSerializer
)

from .models import (
    VisiteVeterinaire
)

from .services import (
    get_dossier_medical,
    get_user_animal,
    ajouter_vaccination,
    ajouter_maladie,
    ajouter_traitement,
    ajouter_visite_veterinaire
)


# ==============================
# DOSSIER MEDICAL
# ==============================

class DossierMedicalDetailView(APIView):

    permission_classes = [IsAuthenticated]


    def get(self, request, animal_id):

        animal = get_user_animal(
            request.user,
            animal_id
        )


        dossier = get_dossier_medical(
            animal.id
        )


        serializer = DossierMedicalSerializer(
            dossier
        )


        return Response(
            serializer.data
        )



# ==============================
# VACCINATIONS
# ==============================

class VaccinationView(APIView):

    permission_classes = [IsAuthenticated]


    def get(self, request, animal_id):

        animal = get_user_animal(
            request.user,
            animal_id
        )


        dossier = get_dossier_medical(
            animal.id
        )


        vaccinations = dossier.vaccinations.all()


        serializer = VaccinationSerializer(
            vaccinations,
            many=True
        )


        return Response(
            serializer.data
        )



    def post(self, request, animal_id):

        animal = get_user_animal(
            request.user,
            animal_id
        )


        dossier = get_dossier_medical(
            animal.id
        )


        serializer = VaccinationSerializer(
            data=request.data
        )


        if serializer.is_valid():

            vaccination = ajouter_vaccination(
                user=request.user,
                dossier=dossier,
                type_vaccin=serializer.validated_data["type_vaccin"],
                date_vaccination=serializer.validated_data["date_vaccination"],
                date_rappel=serializer.validated_data.get("date_rappel")
            )


            return Response(
                VaccinationSerializer(vaccination).data,
                status=status.HTTP_201_CREATED
            )


        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



# ==============================
# MALADIES
# ==============================

class MaladieView(APIView):

    permission_classes = [IsAuthenticated]


    def get(self, request, animal_id):

        animal = get_user_animal(
            request.user,
            animal_id
        )


        dossier = get_dossier_medical(
            animal.id
        )


        maladies = dossier.maladies.all()


        serializer = MaladieSerializer(
            maladies,
            many=True
        )


        return Response(
            serializer.data
        )



    def post(self, request, animal_id):

        animal = get_user_animal(
            request.user,
            animal_id
        )


        dossier = get_dossier_medical(
            animal.id
        )


        serializer = MaladieSerializer(
            data=request.data
        )


        if serializer.is_valid():

            maladie = ajouter_maladie(
                user=request.user,
                dossier=dossier,
                nom=serializer.validated_data["nom"],
                date_diagnostic=serializer.validated_data["date_diagnostic"],
                description=serializer.validated_data.get(
                    "description",
                    ""
                )
            )


            return Response(
                MaladieSerializer(maladie).data,
                status=status.HTTP_201_CREATED
            )


        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



# ==============================
# TRAITEMENTS
# ==============================

class TraitementView(APIView):

    permission_classes = [IsAuthenticated]


    def get(self, request, animal_id):

        animal = get_user_animal(
            request.user,
            animal_id
        )


        dossier = get_dossier_medical(
            animal.id
        )


        traitements = dossier.traitements.all()


        serializer = TraitementSerializer(
            traitements,
            many=True
        )


        return Response(
            serializer.data
        )



    def post(self, request, animal_id):

        animal = get_user_animal(
            request.user,
            animal_id
        )


        dossier = get_dossier_medical(
            animal.id
        )


        serializer = TraitementSerializer(
            data=request.data
        )


        if serializer.is_valid():

            traitement = ajouter_traitement(
                user=request.user,
                dossier=dossier,
                nom=serializer.validated_data["nom"],
                description=serializer.validated_data.get(
                    "description",
                    ""
                ),
                date_debut=serializer.validated_data["date_debut"],
                date_fin=serializer.validated_data.get(
                    "date_fin"
                )
            )


            return Response(
                TraitementSerializer(traitement).data,
                status=status.HTTP_201_CREATED
            )


        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



# ==============================
# VISITES VETERINAIRES
# ==============================

class VisiteVeterinaireView(APIView):

    permission_classes = [IsAuthenticated]


    def get(self, request, animal_id):

        animal = get_user_animal(
            request.user,
            animal_id
        )


        visites = VisiteVeterinaire.objects.filter(
            animal=animal
        )


        serializer = VisiteVeterinaireSerializer(
            visites,
            many=True
        )


        return Response(
            serializer.data
        )



    def post(self, request, animal_id):

        animal = get_user_animal(
            request.user,
            animal_id
        )


        serializer = VisiteVeterinaireSerializer(
            data=request.data
        )


        if serializer.is_valid():

            visite = ajouter_visite_veterinaire(
                user=request.user,
                animal=animal,
                date=serializer.validated_data["date"],
                motif=serializer.validated_data["motif"],
                veterinaire=serializer.validated_data["veterinaire"],
                observations=serializer.validated_data.get(
                    "observations",
                    ""
                )
            )


            return Response(
                VisiteVeterinaireSerializer(visite).data,
                status=status.HTTP_201_CREATED
            )


        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )