from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserRegistrationSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import ProfileSerializer

from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import HistoriqueAction,Historique,User,Licence
from .serializers import HistoriqueActionSerializer


from rest_framework.views import APIView

from .serializers import AdminUserSerializer
from .permissions import IsAdminUser
from .models import Licence
from .serializers import AdminLicenceSerializer

from django.utils import timezone



@csrf_exempt
@api_view(['POST'])
def register(request):

    serializer = UserRegistrationSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response(
            {
                "message": "Compte créé avec succès."
            },
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

def ajouter_historique(user, type_action, details=""):

    historique, created = Historique.objects.get_or_create(
        user=user
    )

    HistoriqueAction.objects.create(
        historique=historique,
        type_action=type_action,
        details=details
    )

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):

        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:

            user = self.serializer_class(
                data=request.data
            )

            if user.is_valid():
                utilisateur = user.user

                ajouter_historique(
                    utilisateur,
                    "LOGIN",
                    "Connexion réussie"
                )

        return response

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        try:
            refresh_token = request.data["refresh"]

            token = RefreshToken(refresh_token)
            token.blacklist()
            ajouter_historique(
                request.user,
                "LOGOUT",
                "Déconnexion réussie"
            )

            return Response(
                {"message": "Déconnexion réussie."},
                status=status.HTTP_205_RESET_CONTENT
            )

        except Exception:
            return Response(
                {"error": "Token invalide."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
class ProfileView(RetrieveUpdateAPIView):

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):

        response = super().update(request, *args, **kwargs)

        ajouter_historique(
            request.user,
            "PROFILE_UPDATE",
            "Modification du profil"
        )

        return response
    

class HistoriqueView(ListAPIView):

    serializer_class = HistoriqueActionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HistoriqueAction.objects.filter(
            historique__user=self.request.user
        ).order_by('-date_action')
    

class AdminUserListView(ListAPIView):

    queryset = User.objects.all()

    serializer_class = AdminUserSerializer

    permission_classes = [IsAdminUser]

class ToggleUserStatusView(APIView):

    permission_classes = [IsAdminUser]


    def patch(self, request, id):

        user = User.objects.get(id=id)

        user.statut_compte = not user.statut_compte

        user.save()

        return Response(
            {
                "message":"Statut utilisateur modifié"
            }
        )
class AdminDeleteUserView(DestroyAPIView):

    queryset = User.objects.all()

    permission_classes = [IsAdminUser]

class AdminLicenceListView(ListAPIView):

    queryset = Licence.objects.all()

    serializer_class = AdminLicenceSerializer

    permission_classes = [IsAdminUser]

class AdminLicenceUpdateView(RetrieveUpdateAPIView):

    queryset = Licence.objects.all()

    serializer_class = AdminLicenceSerializer

    permission_classes = [IsAdminUser]


class AdminDashboardView(APIView):

    permission_classes = [IsAdminUser]


    def get(self, request):

        total_users = User.objects.count()

        active_users = User.objects.filter(
            statut_compte=True
        ).count()

        disabled_users = User.objects.filter(
            statut_compte=False
        ).count()


        today = timezone.now().date()


        active_licenses = Licence.objects.filter(
            date_expiration__gte=today
        ).count()


        expired_licenses = Licence.objects.filter(
            date_expiration__lt=today
        ).count()


        return Response(
            {
                "total_users": total_users,
                "active_users": active_users,
                "disabled_users": disabled_users,
                "active_licenses": active_licenses,
                "expired_licenses": expired_licenses
            }
        )
    
