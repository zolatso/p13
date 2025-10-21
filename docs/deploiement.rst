La chaîne CI/CD pour ce projet utilise **GitHub**, **GitHub Actions** et **Render**.

Étape 1 : Push vers la branche principale
=========================================

À l’heure actuelle, il n’existe qu’une seule branche dans le dépôt, mais nous pourrions en ajouter d’autres à l’avenir.  
Seules les modifications apportées à la branche principale déclenchent le workflow CI/CD.  
Lorsqu’un commit est poussé sur la branche principale, l’action GitHub correspondante est déclenchée.

Étape 2 : GitHub Actions
========================

Cette étape configure un environnement de test, installe les dépendances requises depuis le fichier ``requirements.txt``, puis exécute les tests et le linting.  
Si les tests échouent ou si la couverture des tests n’atteint pas **80 %**, la compilation échoue et le site n’est pas déployé.  
Dans ce cas, vérifiez les problèmes mentionnés et corrigez-les avant de pousser à nouveau.

Étape 3 : Render
================

**Render** gère le déploiement du site en production.  
Chaque fois que **GitHub Actions** exécute avec succès les tests et le linting, **Render** est appelé via un *« deploy hook »* et démarre son propre processus de build.  
Ce processus utilise le fichier **Dockerfile** de production présent dans le dépôt.  
Les variables d’environnement nécessaires sont définies dans l’interface utilisateur de **Render**.
