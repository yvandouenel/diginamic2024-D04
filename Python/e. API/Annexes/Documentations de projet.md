*Exemple de documentation de projet : [début api REST python](https://github.com/Gerob59/fil_rouge_tp7_python/tree/main)*

### Le README.md
---

Le fichier README.md qui se trouve à la racine du projet dois contenir plusieurs parties :
- Une description générale du projet (contexte, le besoin que résout le projet, ...)
- Une description technique du projet (structure du projet, description des dossiers, ...)
- Comment installer le projet
- Comment utiliser le projet
- Les participants (optionnel : les rôles de chacun)

Ceci n'est pas une liste exhaustive, vous pouvez ajouter ou enlever autant de parties en que vous le souhaitez, seulement si cela reste pertinent.

<br>

### Le fichier requirements.txt
---

Ce fichier est à la racine du projet et sert a répertorier tous les modules nécessaire au projet afin des les installer facilement.

> Pour actualiser les modules
```python
pip freeze > requirements.txt
```

> Pour installer les modules
```python
pip install -r requirements.txt
```

<br>

### .gitignore
---

Le fichier `.gitignore` est un fichier à mettre à la racine de son projet.

Il est utilisé pour indiquer à Git quels fichiers et répertoires il doit ignorer lorsqu'il suit les modifications d'un projet. Cela signifie que les fichiers répertoriés dans `.gitignore` ne seront pas inclus dans les commit Git. Il est principalement utilisé pour exclure des fichiers temporaires, des fichiers de compilation, des fichiers sensibles, des fichiers volumineux, des dépendances externes, etc., afin de maintenir un dépôt Git propre et de ne pas encombrer l'historique de version avec des fichiers inutiles.

Exemple : On pourra y mettre le `.env` pour éviter qu'il ne se retrouve sur GitHub.


Il existe un outil en ligne, [gitignore.io](https://www.toptal.com/developers/gitignore/). Il permet de générer un gitignore grâce a des tags, comme python, VisualStudioCode...

<br>

### Le dotenv
---

Une bonne pratique courante et recommandée pour gérer des variables d'environnement dans les projets. Un fichier `.env` permet de stocker des informations sensibles, des clés d'API, des configurations spécifiques à l'environnement, etc., de manière sécurisée et de les charger dans votre application à l'aide de bibliothèques comme `python-decouple` ou `python-dotenv`.

>[!WARNING] `.env` et github
>Ce fichier est surtout utilisé pour caché des informations sensibles, donc il est à éviter de le mettre sur github.
>
>Pour éviter tout problème, il faut ajouter le `.env` au `.gitignore`

<br>

