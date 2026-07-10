
from rest_framework import serializers
from .models import User,HistoriqueAction
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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

        return user
    


class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["email"] = user.email
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name

        return token
    
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