from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput, #change l'affichage en ****
        label="Mot de passe"
    )

    password_confirmation = forms.CharField(
        widget=forms.PasswordInput,
        label="confirmation du mot de passe"
    )

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
        ]

        labels={
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'email': 'Email',
            'genre': 'Genre',
            'telephone': 'Téléphone',
            'adresse': 'Adresse',
            'photo_profil': 'Photo de profil',
        }
    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get(password_confirmation)
    
        if password != password_confirmation:
              raise forms.ValidationError(
                    "Les mots de passe ne correspondent pas."
              )
        return cleaned_data

