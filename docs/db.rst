La structure de la base de données et des modèles de données
============================================================

Il y a trois tables dans notre base de données, et le modèle d’utilisateur Django par défaut est également utilisé.

User
----

Nous utilisons le modèle d’utilisateur Django par défaut pour stocker toutes les informations de base : nom d’utilisateur, adresse e-mail, mot de passe, etc.

Profile
-------

Ce modèle est une extension du modèle d’utilisateur.  
Il a une relation un-à-un avec un utilisateur spécifique — c’est-à-dire qu’un utilisateur a un seul profil, et inversement.  
Le profil contient la ville préférée de l’utilisateur.

Address
-------

Ce modèle spécifie les détails de l’adresse d’une propriété donnée.

Letting
-------

Ce modèle étend le modèle **Address**, avec une relation un-à-un avec **Address**, et inclut également le champ **title** pour la location individuelle.