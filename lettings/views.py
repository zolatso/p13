"""
Module Django définissant les vues pour la gestion des locations (lettings).

Ce module contient :
- index : vue listant toutes les locations disponibles.
- letting : vue affichant le détail d’une location spécifique.
"""

from django.shortcuts import render, get_object_or_404
from .models import Letting


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
    lettings_list = Letting.objects.all()
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
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
