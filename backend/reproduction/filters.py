import django_filters

from .models import Reproduction


class ReproductionFilter(django_filters.FilterSet):

    date_insemination = django_filters.DateFilter(
        field_name="date_insemination"
    )

    date_misebas_prevue = django_filters.DateFilter(
        field_name="date_misebas_prevue"
    )

    mere = django_filters.CharFilter(
        field_name="mere__numero_identification",
        lookup_expr="icontains"
    )


    class Meta:
        model = Reproduction

        fields = [
            "date_insemination",
            "date_misebas_prevue",
            "mere",
        ]