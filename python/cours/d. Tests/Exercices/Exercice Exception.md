**Objectif :** Mettre en pratique la gestion d'erreurs dans les tests unitaires en utilisant `assertRaises`.

**Fonctions à Tester :** La fonction `division_sure` qui prend deux nombres en entrée et renvoie le résultat de la division. La fonction doit lever une exception `ValueError` si le diviseur est égal à zéro.

```python
def division_sure(numerateur, diviseur):
    if diviseur == 0:
        raise ValueError("Le diviseur ne peut pas être zéro.")
    return numerateur / diviseur
```

**Instructions :**

1. Créez une classe de tests appelée `TestDivisionSure` qui hérite de `unittest.TestCase`. Écrivez une méthode de test appelée `test_division_sure`.

2. Utilisez `assertRaises` pour vérifier que l'appel de la fonction `division_sure` avec un diviseur égal à zéro lève bien une exception `ValueError`.

3. Ajoutez un autre test pour vous assurer que la fonction fonctionne correctement lorsque le diviseur n'est pas égal à zéro.

4. Exécutez le test pour vous assurer que la fonction `division_sure` se comporte comme prévu dans les scénarios testés.
