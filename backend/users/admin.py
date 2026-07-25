from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Licence, Historique, HistoriqueAction


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'email',
        'first_name',
        'last_name',
        'statut_compte',
        'is_staff',
        'is_active',
    )

    search_fields = (
        'email',
        'first_name',
        'last_name',
    )

    ordering = (
        'email',
    )


admin.site.register(Licence)
admin.site.register(Historique)
admin.site.register(HistoriqueAction)