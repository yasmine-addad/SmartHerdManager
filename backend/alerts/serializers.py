from rest_framework import serializers
from .models import Alerte


class AlerteSerializer(serializers.ModelSerializer):

    animal = serializers.StringRelatedField()

    class Meta:
        model = Alerte
        fields = '__all__'