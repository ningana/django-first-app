from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Siege(models.Model):

    """
    Cette classe defiie le siége, ou le QG d'un groupe,
    tout ce qui a à savoir sur le siège ud groupe.
    """
    name = models.fields.CharField(max_length=100)
    lieu = models.fields.CharField(max_length=100)
    Creation_Date = models.fields.DateField()

    class Model(models.TextChoices):

        """
        Cette class permet de faire une liste de choix du
        genre de la classe
        """
        VILLA = "VL"
        ENTROPEAU = "EN"
        GARAGE = "GR"
        LYCEE = "LC"
        UNIVERSITY = "UN"
        BATIMENT = "BTN"

    genre = models.fields.CharField(choices=Model.choices, max_length=100)
    number_scoiter = models.fields.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Band(models.Model):

    """
    Cette class definit les caractéristiques d'un groupe musical,
    Quand à la sous classe héritant de models.TextChoices, elle permet
    de creer une liste de choix pour le genre.
    """
    class Genre(models.TextChoices):

        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        REAGUE = 'RG'
        ZOUK_LOVE = 'ZL'
        GOSPEL = 'DL'

    def __str__(self):
        return f'{self.name}'

    name = models.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2022)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    siege = models.ForeignKey(Siege, null=True, on_delete=models.SET_NULL)
    """"Nous pouvons la supprimer avec rm listings/migrations/0009_band_delete_migration
    mais nous allons juste là commenté, et refaire une autre migration"""
    # delete_migration = models.fields.CharField(max_length=50)


class Listing(models.Model):

    """
    Cette class definie Les annonces pour un groupe et la methode
    str permet de convertir l'objet en string sur le site d'administration de Django.
    """
    title = models.fields.CharField(max_length=100)
    year = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2022)]
    )
    description = models.fields.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title}"

    class Type(models.Choices):
        Records = 'Rec'
        Clothing = 'Cl'
        Posters = 'P'
        Miscellaneaous = 'Mis'

    type = models.fields.CharField(choices=Type.choices, max_length=20)
    # Création d'une clé étrangère, ayant pour référence le model Band
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    # delete_also = models.fields.CharField(max_length=50)
    sold = models.fields.BooleanField(default=False)


class Users(models.Model):
    """
    Cette class, ce model, definit les caractéristique d'un user, qui souhaite s'incrire sur le site
    """
    first_name = models.fields.CharField(max_length=30)
    last_name = models.fields.CharField(max_length=30)

    class Sexe(models.Choices):
        Male = "Ml"
        Female = "FM"
        Other = "OT"

    sexe = models.CharField(choices=Sexe.choices, max_length=15)
    if sexe.choices == Sexe.Other:
        sexe = models.CharField(max_length=20)

    class Country(models.Choices):
        Tchad = "+235"
        France = "+33"
        USA = "+1"
        Canada = "+001"
        Chine = "+010"

    contry = models.CharField(choices=Country.choices, max_length=25)
    borned = models.DateField(null=True)
    nationality = models.CharField(max_length=25)
    job = models.CharField(max_length=25)
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}"

    # image = models.ImageField(upload_to=)


class EmailPassword(models.Model):
    Email = models.fields.EmailField()
    Password = models.CharField(max_length=30)
    proprio = models.ForeignKey(Users, null=False, on_delete=models.CASCADE)