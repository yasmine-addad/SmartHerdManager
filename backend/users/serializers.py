
from rest_framework import serializers
from .models import User,Historique,HistoriqueAction
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Licence



class UserRegistrationSerializer(serializers.ModelSerializer):

    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'genre',
            'telephone',
            'adresse',
            'photo_profil',
            'password',
            'password_confirmation'
        ]

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


    def validate(self, data):

        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError(
                "Les mots de passe ne correspondent pas."
            )

        return data


    def create(self, validated_data):

        validated_data.pop('password_confirmation')

        user = User.objects.create_user(
            **validated_data
        )

        Historique.objects.create(
        user=user
        )

        return user
    


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):

        data = super().validate(attrs)


        user = self.user


        data["user"] = {

            "id": user.id,

            "email": user.email,

            "firstName": user.first_name,

            "lastName": user.last_name,

            "role": "admin" if user.is_staff else "manager",

            "isActive": user.is_active,

            "createdAt": user.date_joined

        }


        return data
    
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "genre",
            "telephone",
            "adresse",
            "photo_profil",
        ]
        read_only_fields = ["email"]

class HistoriqueActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoriqueAction
        fields = [
            "id",
            "type_action",
            "details",
            "date_action",
        ]

class AdminUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "telephone",
            "statut_compte",
            "is_staff",
        ]

class AdminLicenceSerializer(serializers.ModelSerializer):

    user_email = serializers.EmailField(
        source="user.email",
        read_only=True
    )

    class Meta:
        model = Licence

        fields = [
            "id",
            "user_email",
            "type",
            "date_debut",
            "date_expiration",
            "statut",
        ]

class AnimalHistoriqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoriqueAction
        fields = [
            "id",
            "type_action",
            "details",
            "date_action",
        ]