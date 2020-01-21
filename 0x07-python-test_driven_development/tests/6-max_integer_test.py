#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_list_num(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        with self.assertRaises(TypeError):
            max_integer([1, 3, 3], 6)
        with self.assertRaises(KeyError):
            max_integer({"hola" : 1, "adios": 2})

    def test_none(self):
        self.assertEqual(max_integer(), None)

    def test_string(self):
        self.assertEqual(max_integer("hola"), "o")

    def test_list_str(self):
        self.assertEqual(max_integer(["aba", "abb", "abc"]), "abc")

    def test_tuple(self):
        self.assertEqual(max_integer(("ab", "ac", "ad")), "ad")
