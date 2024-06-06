
```python
import unittest

def calculate_average(tableau) -> int | float | None:
    if not tableau:
        return None
        
    if not isinstance(tableau, list):
        return None
        
    for element in tableau:
        if isinstance(element, str):
            return None
            
    return sum(tableau) / len(tableau)

class TestCalculateAverage(unittest.TestCase):
    def test_calculate_average(self):
        self.assertEqual(calculate_average([1, 2, 3]), 2)

    def test_calculate_average_float(self):
        self.assertEqual(calculate_average([1, 2, 3.3]), 2.1)

    def test_calculate_average_with_empty_list(self):
        self.assertIsNone(calculate_average([]))

    def test_calculate_average_string(self):
        self.assertIsNone(calculate_average([1, "s", 3.3]))

    def test_calculate_average_str(self):
        self.assertIsNone(calculate_average("s"))
        self.assertEqual(calculate_average("s"), None)

    def test_calculate_average_single_int(self):
        self.assertIsNone(calculate_average(15))

unittest.main()
```
