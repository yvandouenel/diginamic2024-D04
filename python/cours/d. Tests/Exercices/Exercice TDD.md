**Objectif :** Mettre en pratique le Test Driven Development en écrivant des tests unitaires avant d'implémenter la fonction.

**Fonction à Implémenter :** La fonction `calculate_average` qui prend une liste de nombres en entrée et renvoie leur moyenne.

**Instructions :**

1. Commencez par écrire un test unitaire pour la fonction `calculate_average` en utilisant l'approche TDD. Créez une classe de tests appelée `TestCalculateAverage` qui hérite de `unittest.TestCase`. Écrivez une méthode de test appelée `test_calculate_average`.

2. L'étape du test au rouge : Écrivez le test en décrivant le comportement attendu de la fonction `calculate_average`. Par exemple, testez la fonction avec une liste de nombres entiers, de nombres décimaux, et une liste vide.

3. Exécutez le test. Il devrait échouer car la fonction `calculate_average` n'est pas encore implémentée.

4. Passez à l'étape du test au vert : Implémentez la fonction `calculate_average` pour qu'elle passe les tests. N'oubliez pas de retourner la moyenne des nombres dans la liste.

5. Exécutez à nouveau le test pour vous assurer que la fonction `calculate_average` fonctionne correctement.

6. Continuez à ajouter des tests pour différents scénarios (par exemple, gestion des nombres négatifs, gestion des chaînes de caractères, etc.) et implémentez la fonction pour les satisfaire.