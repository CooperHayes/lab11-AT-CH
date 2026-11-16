import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertAlmostEqual(add(12, 2), 14)
        self.assertAlmostEqual(add(-21, 2), -19)
        self.assertAlmostEqual(add(-2, -1), -3)

    def test_subtract(self): # 3 assertions
        self.assertAlmostEqual(subtract(12, 2), 10)
        self.assertAlmostEqual(subtract(-21, 2), -23)
        self.assertAlmostEqual(subtract(-2, -1), -1)
    # ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions

        self.assertAlmostEqual(mul(3,4) , 12)

        self.assertAlmostEqual(mul(-3 , 2) , -6)

        self.assertAlmostEqual(mul(-4 , -5) , 20)

    def test_divide(self): # 3 assertions

        self.assertAlmostEqual(div(2 , 4) , 2.0)

        self.assertAlmostEqual(div(-3 , 15) , -5.0)

        self.assertAlmostEqual(div(-2 , -8) , 4.0)


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 15)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 32), 5)
        self.assertAlmostEqual(logarithm(10, 1000), 3)
        self.assertAlmostEqual(logarithm(3, 81), 4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-5,17)

    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion

        with self.assertRaises(ValueError):
            logarithm(2 , -8)

    def test_hypotenuse(self): # 3 assertions

        self.assertAlmostEqual(hypotenuse(3 , 4) , 5.0)

        self.assertAlmostEqual(hypotenuse(5 , -12) , 13.0)

        self.assertAlmostEqual(hypotenuse(-3 , -4) , 5.0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)

        self.assertAlmostEqual(square_root(9) , 3)

        self.assertAlmostEqual(square_root(0) , 0)


# Do not touch this
if __name__ == "__main__":
    unittest.main()