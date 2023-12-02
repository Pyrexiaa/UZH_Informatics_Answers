import unittest
from unittest import TestCase
from q2 import Publication

class PublicTestSuite(TestCase):

    def test_example(self):
        a = Publication(["A"], "B", 1234)
        b = Publication(["A"], "B", 1234)
        self.assertEqual(a, b)

    def test_str_function(self):
        a = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
        b = """Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"""
        self.assertEqual(str(a), b)

    def test_le_authors(self):
        a = Publication(["F", "S", "A"], "B", 1000)
        b = Publication(["Z", "S", "A"], "Catherine", 1234)
        self.assertLessEqual(a, b)

    def test_le_title(self):
        a = Publication(["A"], "Bob", 1000)
        b = Publication(["A"], "Catherine", 1234)
        self.assertLessEqual(a, b)

    def test_le_year(self):
        a = Publication(["A"], "B", 1000)
        b = Publication(["A"], "B", 1234)
        self.assertLessEqual(a, b)

    def test_ge_authors(self):
        a = Publication(["F", "S", "B"], "B", 1000)
        b = Publication(["E", "S", "A"], "Catherine", 1234)
        self.assertGreaterEqual(a, b)

    def test_ge_title(self):
        a = Publication(["A"], "Zebra", 8888)
        b = Publication(["A"], "Dog", 1234)
        self.assertGreaterEqual(a, b)

    def test_ge_year(self):
        a = Publication(["A"], "B", 8888)
        b = Publication(["A"], "B", 1234)
        self.assertGreaterEqual(a, b)

    def test_lt(self):
        a = Publication(["A"], "B", 1234)
        b = Publication(["A"], "B", 2345)
        self.assertLess(a, b)

    def test_gt(self):
        a = Publication(["A", "B"], "C", 1234)
        b = Publication(["A"], "B", 1234)
        self.assertGreater(a, b)

    def test_ne(self):
        a = Publication(["B"], "C", 1234)
        b = Publication(["A"], "B", 1234)
        self.assertNotEqual(a, b)

if __name__== "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(PublicTestSuite)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
