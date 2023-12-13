from unittest import TestCase
from q5 import calculate_factorial
import unittest

class MyTests(TestCase):

    def test_calculate_factorial(self):
        inp = 5
        expected = 120
        actual = calculate_factorial(inp)
        self.assertEqual(actual, expected)

    def test_string_normal_input(self):
        inp = '5'
        expected = 120
        actual = calculate_factorial(inp)
        self.assertEqual(actual, expected)

    def test_zero_input(self):
        inp = 0
        expected = 1
        actual = calculate_factorial(inp)
        self.assertEqual(actual, expected)

    def test_string_zero_input(self):
        inp = '0'
        expected = 1
        actual = calculate_factorial(inp)
        self.assertEqual(actual, expected)

    def test_negative_input(self):
        inp = -4
        with self.assertRaises(ValueError):
            actual = calculate_factorial(inp)

    def test_string_negative_input(self):
        inp = '-4'
        with self.assertRaises(ValueError):
            actual = calculate_factorial(inp)
        
    def test_large_input(self):
        inp = 15
        with self.assertRaises(ValueError):
            actual = calculate_factorial(inp)

    def test_string_large_input(self):
        inp = '15'
        with self.assertRaises(ValueError):
            actual = calculate_factorial(inp)

    def test_string_input(self):
        inp = "test"
        with self.assertRaises(TypeError):
            actual = calculate_factorial(inp)

    def test_none_input(self):
        inp = None
        expected = None
        actual = calculate_factorial(inp)
        self.assertEqual(actual, expected)

if __name__== "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(MyTests)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
        