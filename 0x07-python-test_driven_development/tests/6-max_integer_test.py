#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Set of tests for max_integer function"""

    def test_simple1(self):
        """ Test for a simple lists"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_simple2(self):
        """ Test for a simple lists"""
        self.assertEqual(max_integer([5, 2, 3, 4]), 5)

    def test_simple3(self):
        """ Test for a simple lists"""
        self.assertEqual(max_integer([4]), 4)

    def test_none(self):
        """ Test for a simple lists"""
        self.assertEqual(max_integer([]), None)

    def test_equal(self):
        """ Test for a simple lists"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_tuple(self):
        """ Test for a simple lists"""
        self.assertEqual(max_integer((1 ,2 ,3 ,4)), 4)

    def test_float(self):
        """ Test for a simple lists"""
        self.assertEqual(max_integer([3.1, 4.6, 2.5, 1.8]), 4.6)

    def test_inf(self):
        """ Test for a simple lists"""
        self.assertEqual(max_integer([1, 2, 3, float("inf")]), float("inf"))

    def test_inf2(self):
        """ Test for a simple lists"""
        self.assertEqual(max_integer([1, 2, 3, float("-inf")]), 3)

    def test_nan(self):
        """ Test for a simple lists"""
        self.assertEqual(max_integer([1, 2, 3, float("nan")]), 3)

    def test_string(self):
        """ Test for a simple lists"""
        self.assertEqual(max_integer(["CDE", "CFH", "CAD"]), "CFH")

    def test_error1(self):
        """ Test for a simple lists"""
        self.assertRaises(TypeError, max_integer, None)

    def test_error2(self):
        """ Test for a simple lists"""
        self.assertRaises(TypeError, max_integer, True)

    def test_error3(self):
        """ Test for a simple lists"""
        self.assertRaises(TypeError, max_integer, [1, [2, 3], 4])

    def test_error4(self):
        """ Test for a simple lists"""
        self.assertRaises(TypeError, max_integer, [1, "CAD"])

    def test_error5(self):
        """ Test for a simple lists"""
        self.assertRaises(TypeError, max_integer, 1)

    def test_error6(self):
        """ Test for a simple lists"""
        self.assertRaises(KeyError, max_integer, {1: 1, 2: 2})
