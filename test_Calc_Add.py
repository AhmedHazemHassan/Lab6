import unittest

class TestCalc_Add(unittest.TestCase):
    def test_add(self): self.assertEqual(TestCalc_Add().add(2, 3), 5)
