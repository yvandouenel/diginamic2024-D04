>[!exemple] **Barème de notation**
>Vous serez évalués selon trois critères principaux :
>
>1. **L'avancement des exercices**
> <br>
> 
>2. **La qualité du code**
>    L'objectif est de rendre le code **lisible**, tant pour **vous** que pour **vos collègues**.
>    - Cela englobe le nommage des variables, la présence de documentation et de commentaires dans votre code, ainsi que la décomposition en fonctions.  
> <br>
> 
>3. **Les points d'effort** / **participation**
>    Cette catégorie vise à récompenser ceux qui sont déterminés à s'améliorer. Ainsi que pour valoriser les personnes qui travaillent en équipe
>    
>    Poser des questions lorsque vous êtes bloqués, **après avoir effectué des recherches par vous-même**.


>[!danger] **Abus**
>
> >L'entraide est autorisée, mais le copier-coller du travail d'autrui est interdit, même si vous avez travaillé ensemble pour résoudre le problème.
> >
> >Réécrire le code vous aidera à mieux le comprendre et vous évitera de nombreux bugs, car chaque personne a son propre style de codage.
>
> > L'utilisation d'IA pour accomplir les exercices à votre place est déconseillée. Faire des erreurs est une part essentielle de l'apprentissage. C'est grâce à ces erreurs que vous apprendrez.

<br>

### Citations d'un écrivain
---

À l'aide du package [`quote`](https://pypi.org/project/quote/), obtenable avec [`pip`](https://pypi.org/project/pip/), extraire 30 citations de Edgar Allan Poe.

>Concevoir un inventaire des titres de livres classés par fréquence d'apparition dans le résultat en ordre décroissant.

>Dresser un inventaire des mots classés par ordre décroissant de présence dans les citations. Ne pas afficher les mots présents moins de 5 fois.

Au moins deux fonctions doivent être créées pour la conception de chacun de ces inventaires.

> [!Tip] Formatage de chaîne de caractères
> **Non obligatoire**
> Le [module 're'](https://docs.python.org/fr/3.11/library/re.html) est utilise pour les expression rationnelle. Exemple : enlever la ponctuation.

<br>

### Titanic
---
À l'aide du module `csv` uniquement, exploiter les données du fichier `titanic_survival.csv` situé dans le dossier "Annexes". Itérer sur les données et montrer les résultats suivants.

> Moyenne d'âge des passagers (~30 ans)

> Pourcentage de survie par classe de passager (~62% pour la première classe, ~43% pour la deuxième classe, ~26% pour la troisième)

> Le bateau de sauvetage ayant sauvé le plus de passagers (bateau n°13 avec 39 passagers sauvés)

<br>

### Exercice supplémentaire
---

| Auteur              |
| ------------------- |
| Edgar Allan Poe     |
| Victor Hugo         |
| Gustave Flaubert    |
| Ernest Hemingway    |
| Agatha Christie     |
| Friedrich Nietzsche |
| Arthur Schopenhauer |
| Simone De Beauvoir  |
| Guy De Maupassant   |
| Voltaire            |
| Emile Zola          |
| Georges Orwell      |
| Frank Herbert       |
| Isaac Asimov        |
| Tolkien             |
| William Shakespeare |

>À partir de la liste des auteurs, et en utilisant uniquement les fonctionnalités natives de Python, générer 30 citations pour chacun de ces auteurs et générer un set des mots en commun à tous ces auteurs.
>
  **Exemple** : si le mot "concombre" est utilisé dans une des citations de Victor Hugo, alors si "concombre" est présent dans une des citations de TOUS les auteurs, il doit être présent dans ce set.

>Faire un classement décroissant des auteurs par le nombre de fois qu'ils utilisent le mot "the" en affichant l'auteur et le nombre de fois que "the" est présent dans ses 30 citations.

>Écrire ce classement dans un fichier csv avec pour noms de colonne "auteur" et "nombre d'occurrences du mot 'the'".

<br>[[Python/a. Impératif/Exercices/Corrections/TP Impératif]]
