**Exemple de Structure :**

```python
import unittest

def reverse_string(s):
    return s[::-1]

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        # Test avec une chaîne normale
        self.assertEqual(reverse_string("hello"), "olleh")

        # Test avec une chaîne numérique
        self.assertEqual(reverse_string("12345"), "54321")

        # Test avec une chaîne contenant des espaces
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_reverse_string_empty(self):
        # Test avec une chaîne vide
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_special_characters(self):
        # Test avec une chaîne contenant des caractères spéciaux
        self.assertEqual(reverse_string("!@#"), "#@!")

if __name__ == '__main__':
    unittest.main()

```