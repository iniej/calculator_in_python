import unittest
import ui



class TestCalculator(unittest.TestCase):

    def test_calculator_addition(self):

        # Test addition function with some data.
        self.assertEqual(7, ui.addition(2,5))
        self.assertEqual(40, ui.addition(15,25))

    def test_calculator_substraction(self):
        # Test addition function with some data.
        self.assertEqual(3, ui.substraction(5,2))
        self.assertEqual(10, ui.substraction(25,15))
        # Test nultiplication fuction withsome data
    def test_calculator_multiplication(self):
        self.assertEqual(10, ui.multiplication(5,2))
        self.assertEqual(250, ui.multiplication(25,10))
        # Test division fuction with some data
    def test_calculator_division(self):
        self.assertEqual(3, ui.division(6,0))
        self.assertEqual(10, ui.division(100,10))


if __name__ == '__main__':
    unittest.main()
