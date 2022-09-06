
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(label="Utilisateur",max_length=50, help_text=None)
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe", max_length=50, help_text=None)


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'sexe',
            'first_name',
            'last_name',
            'email',
            'role',
        )