"""
Module Django définissant les vues pour la gestion des profils utilisateurs.

Ce module contient :
- index : vue listant tous les profils utilisateurs.
- profile : vue affichant le détail d’un profil donné.
"""
import logging

from django.shortcuts import render
from django.http import Http404
from .models import Profile

logger = logging.getLogger(__name__)

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
    try:
        profiles_list = Profile.objects.all()
        if not profiles_list.exists():
            logger.warning("No profiles exist in database")
    except:
        logger.exception("Something went wrong with the DB")
        raise

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
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        logger.warning(
            "User tried to access a profile that does not exist. "
            f"Username submitted = {username}. Returning 404 page."
        )
        raise Http404("Profile not found")
    except Exception:
        logger.exception("Unexpected database error while fetching profile %s", username)
        raise

    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
