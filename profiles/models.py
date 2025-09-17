"""
Module Django définissant le modèle de profil utilisateur.

Ce module contient le modèle Profile, qui étend le modèle User intégré
de Django avec des informations supplémentaires spécifiques à l'application.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Modèle représentant le profil étendu d'un utilisateur.

    Champs :
        user (OneToOneField) : Relation 1:1 avec le modèle User de Django.
        favorite_city (CharField) : Ville préférée de l'utilisateur (optionnelle, max 64 caractères).

    Méthodes :
        __str__ : Retourne le nom d'utilisateur associé au profil.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Retourne le nom d'utilisateur associé au profil.
        """
        return self.user.username
