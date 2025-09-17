from django.shortcuts import render


def index(request):
    """
    Vue affichant la page d'accueil du site.

    Paramètres :
        request (HttpRequest) : Requête HTTP entrante.

    Retour :
        HttpResponse : Page HTML générée via le template "index.html".
    """
    
    return render(request, "index.html")
