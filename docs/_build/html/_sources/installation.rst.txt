Instructions d’installation
===========================

La première étape consiste à cloner le dépôt GitHub sur votre machine locale.

Cloner le dépôt
---------------

.. code-block:: bash

   git clone https://github.com/zolatso/p13.git


Fichier d’environnement
-----------------------

Vous devez créer un fichier ``.env`` à la racine du projet.  
Ce fichier contient des informations sensibles qui ne peuvent pas être partagées dans le dépôt.

Veuillez contacter votre administrateur pour obtenir les valeurs exactes, mais le format du fichier doit être le suivant :

.. code-block:: none

   DJANGO_DEBUG=False
   DJANGO_ALLOWED_HOSTS=localhost
   DJANGO_SECRET_KEY="secret"
   SENTRY_DSN="secret"


Lancer le projet
----------------

Vous pouvez exécuter ce projet soit avec **l’environnement virtuel Python (venv)**, soit avec **l’image Docker** fournie.  

L’utilisation de Docker offre davantage de sécurité et de stabilité à mesure que l’équipe s’agrandit.  
Les instructions pour les deux méthodes sont décrites ci-dessous.


Python venv
-----------

Créer l’environnement virtuel :

.. code-block:: bash

   python3 -m venv env

Activer l’environnement virtuel :

.. code-block:: bash

   source env/bin/activate

Lancer le serveur de développement :

.. code-block:: bash

   python manage.py runserver

Vous pouvez ensuite accéder au site à l’adresse : ``http://localhost:8000``.


Docker
------

Commencez par installer **Docker Desktop** sur votre Mac ou PC.  
Vous devrez également créer un compte Docker.

Une fois Docker Desktop lancé, connectez-vous à votre compte depuis le logiciel ou via la commande suivante :

.. code-block:: bash

   docker login

Si tout fonctionne correctement, exécutez depuis la racine du projet :

.. code-block:: bash

   docker compose up -d

Cette commande vérifie si vous possédez déjà l’image localement.  
Dans le cas contraire, elle la télécharge depuis Docker Hub et démarre le conteneur.  
L’option ``-d`` permet d’exécuter le processus en arrière-plan (mode détaché).

Une fois le conteneur en cours d’exécution, vous pouvez le visualiser dans Docker Desktop.  
Ensuite, accédez à ``http://localhost:8000`` pour voir le site en fonctionnement.

Ajouter un tag à une image Docker et la pousser sur Docker Hub
--------------------------------------------------------------

Si vous avez ajouté une nouvelle dépendance dans le fichier ``requirements.txt`` ou effectué d’autres modifications, vous pouvez ajouter un tag à l’image Docker et la pousser vers le dépôt Docker Hub.  
De cette manière, les autres membres de l’équipe pourront accéder à la version contenant les dernières modifications.


   Utilisez la commande suivante pour créer un nouveau tag associé à votre image :

   .. code-block:: bash

      docker tag <nom_image>:<ancien_tag> <nom_utilisateur_dockerhub>/<nom_image>:<nouveau_tag>

**Pousser l’image sur Docker Hub :**

   .. code-block:: bash

      docker push <nom_utilisateur_dockerhub>/<nom_image>:<nouveau_tag>

L’image est maintenant disponible sur Docker Hub sous le dépôt spécifié.