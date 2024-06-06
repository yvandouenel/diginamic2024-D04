**Objectif :** Écrire des tests unitaires pour une fonction de manipulation de chaînes.

**Fonction à Tester :** La fonction `reverse_string` qui prend une chaîne de caractères en entrée et renvoie sa version inversée.

```python
def reverse_string(s):
    return s[::-1]
```

> [!TIP] Regle de nommage
> Assurez-vous de suivre la convention de nommage en préfixant le nom de votre méthode de test par `test_`.

**Instructions :**

1. Créez une classe de tests appelée `TestReverseString` qui hérite de `unittest.TestCase`.

2. Écrivez une méthode de test appelée `test_reverse_string` dans la classe `TestReverseString`. Cette méthode devrait tester la fonction `reverse_string` pour différents scénarios.

3. Ajoutez une nouvelle méthode de test appelée `test_reverse_string_empty` pour tester le comportement de la fonction avec une chaîne vide.

4. Ajoutez une nouvelle méthode de test appelée `test_reverse_string_special_characters` pour tester le comportement de la fonction avec une chaîne contenant des caractères spéciaux.

5. Exécutez vos tests pour vous assurer que les fonctions fonctionne correctement dans divers scénarios.

[[correction test unitaire]]