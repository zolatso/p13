Technologies et les langages de programmation à utiliser
========================================================


Python/Django
--------------

Le framework qui se connecte à la base de données, gère le routage des URL et prépare les pages via les *views* et les *templates*.  
Django est un framework hautement évolutif qui permettra au site web de se développer à mesure que de nouvelles fonctionnalités seront ajoutées.

Sentry
------

Cet outil de surveillance des erreurs fournit un registre centralisé de toutes les erreurs et des problèmes rencontrés par les utilisateurs sur le site (y compris ceux que nous avons spécifiés avec la bibliothèque de journalisation de Python).  
Cela nous permet de suivre en temps réel les problèmes rencontrés par les utilisateurs et d’ajuster le site en conséquence.

GitHub Actions
--------------

C’est un élément clé du pipeline d’intégration et de déploiement continus (*CI/CD*).  
Chaque fois qu’un *commit* est poussé sur la branche principale, une action est déclenchée : elle configure un environnement de test, exécute les tests et applique le *linting*.  
Si tout se déroule sans problème, le site est déployé sur Render via un *deploy hook*.  

Si l’une des conditions suivantes se produit :  
a) les tests échouent,  
b) la couverture des tests n’atteint pas 80 %, ou  
c) le *linting* échoue,  
alors le déploiement n’a pas lieu.

Docker
------

Docker nous permet de disposer d’un environnement propre aussi bien pour le développement que pour la production.  
Une image Docker est stockée sur Docker Hub et sert à construire l’environnement Docker localement.  

Dans notre configuration particulière, cette image Docker n’est pas utilisée en production ; Render construit sa propre image/conteneur Docker à partir du fichier *Dockerfile* de production stocké dans le dépôt.  

En principe, on pourrait utiliser la même image Docker pour le développement local, les tests dans GitHub Actions et le déploiement sur Render, bien que cela n’apporte pas d’avantages particuliers pour ce projet.
