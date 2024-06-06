```python
import unittest

def division_sure(numerateur, diviseur):
    if diviseur == 0:
        raise ValueError("Le diviseur ne peut pas être zéro.")
    return numerateur / diviseur

class TestDivisionSure(unittest.TestCase):
    def test_division_sure(self):
        # Test avec un diviseur égal à zéro (doit lever une exception ValueError)
        with self.assertRaises(ValueError):
            division_sure(10, 0)

        # Test avec des valeurs normales (doit fonctionner sans exception)
        result = division_sure(10, 2)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
```