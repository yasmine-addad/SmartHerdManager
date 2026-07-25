from rest_framework import serializers
from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = [
            'id',
            'numero_identification',
            'espece',
            'race',
            'sexe',
            'date_naissance',
            'poids',
            'statut',
            'photo',
            'proprietaire'
        ]
        read_only_fields = ['proprietaire']