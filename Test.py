import unittest
from Calculator import Calculator
class Test(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_add(self):
        self.assertEqual(self.calculator.add(3,7), 10)
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(6,2),4)
    def test_multiply(self):
            self.assertEqual(self.calculator.multiply(5, 6), 30)
    def test_divide(self):
            self.assertEqual(self.calculator.divide(82, 16), 5.125)
    def test_exponentiation(self):
            self.assertEqual(self.calculator.exponentiation(3,2), 9)
if __name__ == "__main__":
     unittest.main()

