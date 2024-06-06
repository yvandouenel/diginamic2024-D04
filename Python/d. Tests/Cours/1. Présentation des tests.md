Pourquoi les tests sont essentiels. Construiriez vous une maison sans vous assurer que chaque partie fonctionne correctement ? Les tests sont les gardiens de la solidité de nos projets, et nous allons découvrir comment les utiliser efficacement.

Au cours de cette période, nous allons explorer divers types de tests, des fonctionnels aux non fonctionnels, en passant par les principes fondamentaux et des concepts avancés. Les tests ne sont pas une formalité, mais des outils puissants pour améliorer la qualité de nos productions.

![testing mentality](https://miro.medium.com/v2/resize:fit:1200/1*rqBe467chY83XWjl6EkUvg.jpeg)

<br>

## Panorama des types de tests

---

On peut représenter les blocs principaux des tests grâce à une pyramide allant de 3 à 5 blocs environs, mais en majorité 4.
- Plus on est bas dans la pyramide, plus les tests sont légions car ils sont moins chère, plus rapide à faire et permettent une meilleur isolation des composants.
- Plus on est haut, plus les tests se rarifient, car ils coutent chères, sont lents à entreprendre et font intervenir plusieurs acteurs. On test la globalité du programme.

En plus de ces tests, on peut en retrouver des transverses qui vont vérifier sur plusieurs couchent.

![pyramide de tests](https://kalisoft.fr/wp-content/uploads/2021/05/nt-1024x568.png)

### **Tests unitaires :**
> Tests automatisés qui évaluent le bon fonctionnement des unités individuelles de code, comme des fonctions ou des méthodes. L'objectif est de s'assurer que chaque unité fonctionne correctement de manière isolée.

### **Tests d'intégration :**
> Evaluent la manière dont les différentes unités de code interagissent entre elles. L'objectif est de détecter les erreurs qui pourraient survenir lorsque les unités sont combinées.

### **Tests système :**
> Vérifient que l'ensemble du système, ou une application, fonctionne conformément aux spécifications. Cela inclut la vérification des interactions entre les composants et la validation des fonctionnalités dans un environnement proche de la production.

### **Tests d'acceptation :**
> Effectués pour déterminer si un système satisfait les critères d'acceptation convenus. Ils sont souvent réalisés en collaboration avec les parties prenantes pour garantir que le système répond aux besoins métier.

<br>

## But des Tests

---

Les tests existent pour assurer la fiabilité et la robustesse du code, agissant comme des filets de sécurité. Ils garantissent que chaque élément contribue cohéremment au projet.

### Fiabilité et Robustesse
- **Définition du but des tests :** Assurer que chaque ligne de code répond aux attentes.
- **Application :** Illustration avec des exemples concrets.
- **Détection de Failles :** Les tests ne valident pas seulement le bon fonctionnement, ils exposent ce qui pourrait ne pas fonctionner correctement.

Cette section clarifie le rôle essentiel des tests dans la construction de logiciels fiables et robustes, préparant à aborder des concepts plus avancés.

<br>
### <u>Exemple : Ariane 5</u>

Le 4 juin 1996, le vol 501 de la nouvelle fusée Ariane 5 s’est soldé par une explosion en plein vol, 36,7 secondes seulement après le décollage.

![ariane 5](https://printf.eu/wp-content/uploads/2014/04/wpid-ariane-5-300x223.jpg)

Sauf que cette impressionnante explosion ne fait pas suite à un problème matériel. il s’agit en fait d’un simple dépassement d’entier ! codé sur 8 bits **la variable est passée à 256, puis non pas à 257, mais à 0**.
<br>

## Dette Technique, Tests de Non-Régression

---
### Dette technique
- **Définition :** Compréhension de la dette technique et son impact.
- **Gestion :** Prévention, résolution, exemples concrets dans des projets académiques.

### Tests de non-régression
- **Concept :** Assurer la stabilité malgré l'évolution du logiciel.
- **Stratégies :** Comment intégrer les tests de non-régression dans les itérations.

<br>

## Définition du Risque (Impact * Probabilité)

---

En donnant les facteurs de Probabilité et d'Impact aux possibles risques du projet, on peut prévoir à l'avance les conséquences et donc prévoir des mesures afin de le contrecarré.

![Matrice  de risque](https://webusupload.apowersoft.info/gitmind/wp-content/uploads/2022/05/risk-map-1.jpg)

<u>Exemple :</u>
- Une météorite nous tombe dessus. (Probabilité : improbable, Impact : Catastrophique)
- Un collaborateur tombe malade (Probabilité : Occasionnel, Impact : Considérable)

Même si l'impact est moins élevé, le collaborateurs malade est plus possible et plus contraignant que la météorite, car il a une probabilité plus élevé. On peut aussi plus facilement prendre des mesures pour le contrer.