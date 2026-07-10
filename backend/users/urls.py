from django.urls import path
from . import views
from .views import LogoutView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import LoginView

from .views import ProfileView

from .views import HistoriqueView

from .views import (
    AdminUserListView,
    ToggleUserStatusView,
    AdminDeleteUserView
)

from .views import (
    AdminLicenceListView,
    AdminLicenceUpdateView
)

from .views import AdminDashboardView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path(
    "history/",
    HistoriqueView.as_view(),
    name="history"
    ),
    path(
    "admin/users/",
    AdminUserListView.as_view()
    ),

    path(
    "admin/users/<int:id>/status/",
    ToggleUserStatusView.as_view()
    ),

    path(
    "admin/users/<int:pk>/delete/",
    AdminDeleteUserView.as_view()
    ),

    path(
    "admin/licenses/",
    AdminLicenceListView.as_view()
    ),

    path(
    "admin/licenses/<int:pk>/",
    AdminLicenceUpdateView.as_view()
    ),

    path(
    "admin/dashboard/",
    AdminDashboardView.as_view(),
    name="admin-dashboard"
    ),
]
