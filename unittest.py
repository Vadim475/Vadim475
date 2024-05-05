import unittest

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(6, 0)

    def test_exponentiate(self):
        self.assertEqual(self.calc.exponentiate(2, 3), 8)

    def test_integer_division(self):
        self.assertEqual(self.calc.integer_division(7, 3), 2)

    def test_remainder(self):
        self.assertEqual(self.calc.remainder(7, 3), 1)

if __name__ == "__main__":
    unittest.main()
