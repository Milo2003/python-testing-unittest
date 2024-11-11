import unittest
from src.calculator import sum, subtract, multiply, divide


class CalculatorTest(unittest.TestCase):
    def test_sum(self):
        assert sum(2, 2) == 4

    def test_subtract(self):
        assert subtract(2, 2) == 0

    def test_multiply(self):
        assert multiply(2, 3) == 6

    def test_division(self):
        assert divide(4, 2) == 2

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(4, 0)


if __name__ == "__main__":
    unittest.main()
