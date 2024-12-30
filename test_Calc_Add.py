import unittest
from Calc_Add import Calculator_function

calc = Calculator_function()

class TestCalc_Add(unittest.TestCase):
    def test_add(self): self.assertEqual(calc.add(2, 3), str(5))
    def test_add(self): self.assertEqual(calc.add(-1, 1), str(0))
    def test_add(self): self.assertEqual(calc.add(100, 200), str(300))
