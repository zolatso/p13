"""
Application Django : Profiles

Cette application gère les profils utilisateurs étendus, liés au modèle User intégré de Django.

Contenu :
- models.py : définit le modèle Profile, avec des informations supplémentaires
  comme la ville préférée de l'utilisateur.
- views.py : contient les vues permettant d’afficher la liste des profils
  et le détail d’un profil spécifique.
- templates/profiles/ : répertoire des templates HTML associés aux vues.

Utilisation :
- L’application permet de stocker et afficher des informations supplémentaires
  sur les utilisateurs, en plus des données fournies par le modèle User de Django.
"""