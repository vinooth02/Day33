import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(10, 20)
        self.assertEqual(result, 30)

    def test_subtract(self):
        result = self.calculator.subtract(20, 10)
        self.assertEqual(result, 10)

    def test_multiply(self):
        result = self.calculator.multiply(10, 5)
        self.assertEqual(result, 50)

    def test_divide(self):
        result = self.calculator.divide(20, 5)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()