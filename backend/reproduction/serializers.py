from rest_framework import serializers

from .models import (
    Reproduction,
    Naissance
)


class ReproductionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reproduction
        fields = "__all__"
        read_only_fields = (
            "date_misebas_prevue",
        )


class NaissanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Naissance
        fields = "__all__"