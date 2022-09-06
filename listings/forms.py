from django import forms     # Module de formulaire
from . models import Band, Listing
from . models import Users
from . models import EmailPassword


class ContactUsForm(forms.Form):
    """
    Classe de formulaire de django
    """
    name = forms.CharField(required=True)  # Pour les formulaires, un Charfield est optionel
    email = forms.EmailField(help_text="Your email please, with a @ right")
    """
    On appliquer des widgets à n'importe quel champ du formualire"""
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    message = forms.CharField(widget=forms.Textarea,max_length=1000)


class BandForm(forms.ModelForm):
    """
    Classe nous permetra de creer un formulaire de model automatiquement
    """
    class Meta:
        model = Band
        # fields = '__all__' , c'était comme ça avant
        """
        Nous pouvons également exclure des champs, que seul
        nous pouvons modifier"""
        exclude = ('active', 'official_homepage')
        """
        Nous pouvons exclure autant de champ que nous voulons, seluement, on se rassure 
        qu'ils ont une valuer null ou une valeur par defaut ...
        Sinon, nous les modifions, et exécuter les migrations"""


class ListingForm(forms.ModelForm):
    """
    Creation du formlaire du model Listing pour les utilisateurs
    """
    class Meta:
        model = Listing
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'


class Emailpassword(forms.ModelForm):
    class Meta:
        model = EmailPassword
        fields = '__all__'