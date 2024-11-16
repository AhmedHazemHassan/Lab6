import unittest

class TestCalc_Add(unittest.TestCase):
    def test_add(self): self.assertEqual(Calculator().add(2, 3), 5)
