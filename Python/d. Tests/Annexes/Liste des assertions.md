| Méthode                                     | Explication                                                   |
| -------------------------------------------- | ------------------------------------------------------------ |
| `self.assertEqual(a, b)`                     | Vérifie si `a` est égal à `b`.                               |
| `self.assertNotEqual(a, b)`                  | Vérifie si `a` n'est pas égal à `b`.                          |
| `self.assertTrue(expr)`                      | Vérifie si l'expression `expr` est vraie.                    |
| `self.assertFalse(expr)`                     | Vérifie si l'expression `expr` est fausse.                   |
| `self.assertIn(item, container)`             | Vérifie si `item` est dans `container`.                      |
| `self.assertNotIn(item, container)`          | Vérifie si `item` n'est pas dans `container`.                |
| `self.assertIsInstance(obj, cls)`           | Vérifie si `obj` est une instance de la classe `cls`.        |
| `self.assertNotIsInstance(obj, cls)`        | Vérifie si `obj` n'est pas une instance de la classe `cls`. |
| `self.assertIs(a, b)`                        | Vérifie si `a` est identique à `b` (même objet en mémoire). |
| `self.assertIsNot(a, b)`                     | Vérifie si `a` n'est pas identique à `b` (objets différents en mémoire). |
| `self.assertIsNone(expr)`                    | Vérifie si `expr` est `None`.                                |
| `self.assertIsNotNone(expr)`                 | Vérifie si `expr` n'est pas `None`.                          |
| `self.assertRaises(exception, callable, *args, **kwargs)` | Vérifie si l'appel de la fonction `callable` avec les arguments spécifiés lève l'exception spécifiée. |
| `self.assertGreater(a, b)`                   | Vérifie si `a` est strictement supérieur à `b`.             |
| `self.assertGreaterEqual(a, b)`              | Vérifie si `a` est supérieur ou égal à `b`.                 |
| `self.assertLess(a, b)`                      | Vérifie si `a` est strictement inférieur à `b`.             |
| `self.assertLessEqual(a, b)`                 | Vérifie si `a` est inférieur ou égal à `b`.                |
| `self.assertAlmostEqual(a, b)`              | Vérifie si `a` est approximativement égal à `b`.           |
| `self.assertNotAlmostEqual(a, b)`           | Vérifie si `a` n'est pas approximativement égal à `b`.    |
