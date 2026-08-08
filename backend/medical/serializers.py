from rest_framework import serializers

from .models import (
    DossierMedical,
    Vaccination,
    Maladie,
    Traitement,
    VisiteVeterinaire
)


class VaccinationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vaccination
        fields = "__all__"
        read_only_fields = ["dossier_medical"]

    def validate(self, data):

        date_rappel = data.get("date_rappel")

        if (
            date_rappel
            and date_rappel < data["date_vaccination"]
        ):
            raise serializers.ValidationError(
                "La date de rappel doit être postérieure à la date de vaccination."
            )

        return data


class MaladieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Maladie
        fields = "__all__"
        read_only_fields = ["dossier_medical"]


class TraitementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Traitement
        fields = "__all__"
        read_only_fields = ["dossier_medical"]

    def validate(self, data):

        date_fin = data.get("date_fin")

        if (
            date_fin
            and date_fin < data["date_debut"]
        ):
            raise serializers.ValidationError(
                "La date de fin doit être postérieure à la date de début."
            )

        return data


class VisiteVeterinaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = VisiteVeterinaire
        fields = "__all__"
        read_only_fields = ["animal"]


class DossierMedicalSerializer(serializers.ModelSerializer):

    vaccinations = VaccinationSerializer(
        many=True,
        read_only=True
    )

    maladies = MaladieSerializer(
        many=True,
        read_only=True
    )

    traitements = TraitementSerializer(
        many=True,
        read_only=True
    )

    visites_veterinaires = VisiteVeterinaireSerializer(
        many=True,
        read_only=True,
        source="animal.visites_veterinaires"
    )

    class Meta:

        model = DossierMedical

        fields = [
            "id",
            "animal",
            "created_at",
            "updated_at",
            "vaccinations",
            "maladies",
            "traitements",
            "visites_veterinaires"
        ]

        read_only_fields = [
            "animal",
            "created_at",
            "updated_at"
        ]