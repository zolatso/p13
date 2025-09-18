"""
Module Django définissant les vues pour la gestion des locations (lettings).

Ce module contient :
- index : vue listant toutes les locations disponibles.
- letting : vue affichant le détail d’une location spécifique.
"""
import logging

from django.shortcuts import render
from django.http import Http404
from .models import Letting

logger = logging.getLogger(__name__)

def index(request):
    """
    Vue affichant la liste de toutes les locations.

    Paramètres :
        request (HttpRequest) : Requête HTTP entrante.

    Contexte :
        lettings_list (QuerySet) : Ensemble des objets Letting.

    Retour :
        HttpResponse : Page HTML générée affichant toutes les locations
        via le template "lettings/index.html".
    """
    try:
        lettings_list = Letting.objects.all()
        if not lettings_list.exists():
            logger.warning("No lettings exist in database")
    except Exception as e:
        logger.exception("Error while accessing all lettings in database.")
        raise

    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Vue affichant le détail d’une location donnée.

    Paramètres :
        request (HttpRequest) : Requête HTTP entrante.
        letting_id (int) : Identifiant unique de la location à afficher.

    Contexte :
        title (str) : Titre de la location.
        address (Address) : Adresse associée à la location.

    Retour :
        HttpResponse : Page HTML générée affichant les détails de la
        location via le template "lettings/letting.html".
    """
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        logger.warning(
            "User tried to access a letting that does not exist. "
            f"ID submitted = {letting_id}. Returning 404 page."
        )
        raise Http404("Letting not found")
    except Exception:
        logger.exception("Unexpected database error while fetching letting %s", letting_id)
        raise

    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
