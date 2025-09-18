"""
Module Django définissant les modèles liés aux adresses et aux locations immobilières.

Ce module contient deux modèles principaux :
- Address : représente une adresse postale complète avec validations.
- Letting : représente une location (logement, bien immobilier) associée à une adresse unique.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle représentant une adresse postale.

    Champs :
        number (PositiveIntegerField) : Numéro de voie, limité à 4 chiffres maximum.
        street (CharField) : Nom de la rue, limité à 64 caractères.
        city (CharField) : Ville, limitée à 64 caractères.
        state (CharField) : Code de l’État/région sur 2 caractères.
        zip_code (PositiveIntegerField) : Code postal, limité à 5 chiffres maximum.
        country_iso_code (CharField) : Code pays ISO (3 lettres obligatoires).

    Méthodes :
        __str__ : Retourne une représentation textuelle sous la forme "numéro rue".
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        """
        Retourne une chaîne descriptive de l’adresse.
        Exemple : "12 Rue de la Paix".
        """
        return f"{self.number} {self.street}"

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Modèle représentant une location immobilière.

    Champs :
        title (CharField) : Titre ou nom de la location, limité à 256 caractères.
        address (OneToOneField) : Relation 1:1 vers le modèle Address.

    Méthodes :
        __str__ : Retourne le titre de la location.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retourne le titre de la location.
        """
        return self.title
