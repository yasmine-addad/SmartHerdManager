from django.contrib import admin
from .models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):

    list_display = (
        'numero_identification',
        'espece',
        'race',
        'sexe',
        'poids',
        'statut',
    )

    search_fields = (
        'numero_identification',
        'espece',
        'race',
    )

    list_filter = (
        'espece',
        'race',
        'statut',
    )

    ordering = (
        'numero_identification',
    )

