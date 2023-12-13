import unittest
from unittest import TestCase
from q4 import evolve

# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class ConwayGameOfLifeTests(TestCase):

    def test_glider(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        expected = ((
            "--------------",
            "| ###        |",
            "| #          |",
            "|  #         |",
            "|            |",
            "|            |",
            "--------------"
        ), 5)
        actual = evolve(field, 4)
        self.assertEqual(actual, expected)

    def test_stable_structure(self):
        field = (
            "---------------",
            "|             |",
            "|  ##         |",
            "|  ##         |",
            "|             |",
            "|             |",
            "---------------"
        )
        expected = ((
            "---------------",
            "|             |",
            "|  ##         |",
            "|  ##         |",
            "|             |",
            "|             |",
            "---------------"
        ), 4)
        actual = evolve(field, 5)
        self.assertEqual(actual, expected)

    def test_oscillator(self):
        field = (
            "---------------",
            "|             |",
            "|   #         |",
            "|   #         |",
            "|   #         |",
            "|             |",
            "---------------"
        )
        expected = ((
            "---------------",
            "|             |",
            "|   #         |",
            "|   #         |",
            "|   #         |",
            "|             |",
            "---------------"
        ), 3)
        actual = evolve(field, 4)
        self.assertEqual(actual, expected)

    def test_empty_field(self):
        field = (
            "------",
            "|    |",
            "|    |",
            "|    |",
            "|    |",
            "|    |",
            "------"
        )
        expected = ((
            "------",
            "|    |",
            "|    |",
            "|    |",
            "|    |",
            "|    |",
            "------"
        ), 0)
        actual = evolve(field, 3)
        self.assertEqual(actual, expected)

    def test_non_tuple(self):
        field = {
            "------",
            "|    |",
            "|    |",
            "|    |",
            "|    |",
            "|    |",
            "------"
        }
        with self.assertRaises(Warning):
            evolve(field, 3)

    def test_invalid_character(self):
        field = (
            "------",
            "|    |",
            "|    |",
            "|    |",
            "|  x |",
            "|    |",
            "------"
        )
        with self.assertRaises(Warning):
            evolve(field, 3)

    def test_not_same_row_length(self):
        field = (
            "------",
            "|     |",
            "|     |",
            "|    |",
            "|    |",
            "|    |",
            "------"
        )
        with self.assertRaises(Warning):
            evolve(field, 3)

    def test_non_integer_steps(self):
        field = (
            "------",
            "|    |",
            "|    |",
            "| ## |",
            "|  # |",
            "|    |",
            "------"
        )
        with self.assertRaises(Warning):
            evolve(field, -3)
    
    def test_zero_row(self):
        field = ()
        with self.assertRaises(Warning):
            evolve(field, 3)
    

if __name__== "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(ConwayGameOfLifeTests)
    unittest.TextTestRunner(verbosity=2).run(test_suite)