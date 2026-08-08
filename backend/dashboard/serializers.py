from rest_framework import serializers


class DashboardSerializer(serializers.Serializer):

    animaux_par_espece = serializers.ListField()

    femelles_gestantes = serializers.IntegerField()

    animaux_malades = serializers.IntegerField()

    animaux_en_traitement = serializers.IntegerField()

    naissances_mois = serializers.IntegerField()