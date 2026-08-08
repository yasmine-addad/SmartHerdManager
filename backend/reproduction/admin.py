from django.contrib import admin

from .models import Reproduction, Naissance


@admin.register(Reproduction)
class ReproductionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "mere",
        "date_insemination",
        "date_misebas_prevue",
        "date_misebas_reelle",
    )

    search_fields = (
        "mere__numero_identification",
        "mere__race",
        "mere__espece",
    )

    list_filter = (
        "date_insemination",
        "date_misebas_prevue",
        "date_misebas_reelle",
    )

    ordering = ("-date_insemination",)


@admin.register(Naissance)
class NaissanceAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "reproduction",
        "animal_enfant",
        "date_naissance",
    )

    search_fields = (
        "animal_enfant__numero_identification",
        "reproduction__mere__numero_identification",
    )

    list_filter = (
        "date_naissance",
    )

    ordering = ("-date_naissance",)