import unittest
from unittest import TestCase
from q3 import sort

# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class SortTests(TestCase):

    def test_sort_ascending_order(self):
        # Test sorting in ascending order
        test_cases = [
            ([4, 2, 7, 1], [1, 2, 4, 7]),
            ([5, 5, 5, 5], [5, 5, 5, 5]),
            ([9, 3, 6, 0], [0, 3, 6, 9]),
            (['banana', 'apple', 'cherry'], ['apple', 'banana', 'cherry']),
            ([], []),
            ((4, 2, 7, 1), [1, 2, 4, 7]),  # Test with tuple input
        ]

        for input_list, expected_output in test_cases:
            with self.subTest(input_list=input_list):
                self.assertEqual(sort(input_list), expected_output)

    # Test if the function returns a new list
    def test_sort_returns_new_list(self):
        input_list = [4, 2, 7, 1]
        sorted_list = sort(input_list)
        self.assertIsNot(sorted_list, input_list)

    # Test with non-iterable input
    def test_sort_non_iterable_input(self):
        non_iterable_inputs = [None, 5]
        for input_value in non_iterable_inputs:
            with self.subTest(input_value=input_value):
                self.assertIsNone(sort(input_value))

if __name__== "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(SortTests)
    unittest.TextTestRunner(verbosity=2).run(test_suite)