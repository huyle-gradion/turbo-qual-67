import unittest
from src.calc import add, multiply, power

class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
    def test_power(self):
        self.assertEqual(power(2, 3), 8)

if __name__ == "__main__":
    unittest.main()
