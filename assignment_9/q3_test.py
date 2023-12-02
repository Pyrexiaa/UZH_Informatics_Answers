import unittest
from unittest import TestCase
from q3 import Matrix

class MatrixTestCase(TestCase):
    def test_addition(self):
        a = Matrix(
            [[1,2],
            [3,4]])
        b = Matrix(
            [[1,2],
            [3,4]])
        result = Matrix(
                [[2,4],
                [6,8]])
        self.assertEqual(a+b, result)

    def test_multiplication(self):
        a = Matrix(
            [[1,2],
            [3,4]])
        b = Matrix(
            [[1,2],
            [3,4]])
        result = Matrix(
                [[7,10],
                [15,22]])
        self.assertEqual(a*b, result)

    def test_multiplication2(self):
        a = Matrix(
            [[1,2],
            [3,4]])
        b = Matrix(
            [[1],
            [10]])
        result = Matrix(
                [[21],
                [43]])
        self.assertEqual(a*b, result)

    def test_not_equal(self):
        a = Matrix(
            [[1],
            [3]])
        b = Matrix(
            [[1],
            [10]])
        self.assertNotEqual(a, b)

    def test_equal(self):
        a = Matrix(
            [[1],
            [3]])
        b = Matrix(
            [[1],
            [3]])
        self.assertEqual(a, b)

    def test_hashable(self):
        a = Matrix(
            [[1, 2],
             [3, 4]])
        b = Matrix(
            [[1, 2], 
             [3, 4]])
        c = Matrix(
            [[2, 3], 
             [4, 5]])

        matrix_dict = {a: "A", b: "A", c: "C"}

        self.assertEqual(matrix_dict[a], "A")
        self.assertEqual(matrix_dict[b], "A")
        self.assertEqual(matrix_dict[c], "C")
        self.assertEqual(len(matrix_dict), 2)

if __name__== "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(MatrixTestCase)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
