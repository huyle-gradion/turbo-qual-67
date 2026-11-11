import unittest
from src.calc import add, multiply, subtract, power

class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
    def test_power(self):
        self.assertEqual(power(2, 3), 8)

if __name__ == "__main__":
    unittest.main()

# competing base advance feat/qual-20261111-102655-ab284c-sc3-advance
