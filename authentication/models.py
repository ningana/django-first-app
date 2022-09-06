from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """
    This class define all the type of our user, kind the name ...
    """
    # choices list for user, of course, we can also do it with a subclass
    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )

    picture = models.ImageField(verbose_name='Photo de profile', null=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')

    class Sexe(models.Choices):
        MALE = "MS"
        FEMALE = "FM"
        OTHER = "OT"

    sexe = models.CharField(max_length=20, choices=Sexe.choices, blank=True, null=True)

    def __str__(self):
        return self.username