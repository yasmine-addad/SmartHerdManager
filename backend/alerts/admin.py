from django.contrib import admin
from .models import Alerte


@admin.register(Alerte)
class AlerteAdmin(admin.ModelAdmin):

    list_display = (
        'titre',
        'animal',
        'type_alerte',
        'date_alerte',
        'statut'
    )

    list_filter = (
        'type_alerte',
        'statut'
    )

    search_fields = (
        'animal__numero_identification',
        'titre'
    )