"""
Module Django définissant les vues pour la gestion des profils utilisateurs.

Ce module contient :
- index : vue listant tous les profils utilisateurs.
- profile : vue affichant le détail d’un profil donné.
"""

from django.shortcuts import render, get_object_or_404
from .models import Profile


def index(request):
    """
    Vue affichant la liste de tous les profils utilisateurs.

    Paramètres :
        request (HttpRequest) : Requête HTTP entrante.

    Contexte :
        profiles_list (QuerySet) : Ensemble des objets Profile.

    Retour :
        HttpResponse : Page HTML générée affichant tous les profils
        via le template "profiles/index.html".
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Vue affichant le détail d’un profil utilisateur donné.

    Paramètres :
        request (HttpRequest) : Requête HTTP entrante.
        username (str) : Nom d'utilisateur dont on souhaite afficher le profil.

    Contexte :
        profile (Profile) : Objet Profile associé à l'utilisateur.

    Retour :
        HttpResponse : Page HTML générée affichant les détails du profil
        via le template "profiles/profile.html".
    """
    # profile = Profile.objects.get(user__username=username)
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}

    return render(request, "profiles/profile.html", context)
