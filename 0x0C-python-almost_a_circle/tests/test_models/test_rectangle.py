#!/usr/bin/python3
""" Unit test for base model file """
import unittest
from models.rectangle import Rectangle


class test_RectangleModel(unittest.TestCase):
    """ Tests of the model Rectangle"""
    def test_id(self):
        """ test ids of the base model"""
        b3 = Rectangle(1, 2)
        self.assertEqual(b3.id, 4)
        b2 = Rectangle(1, 2, 4, 3, 54)
        self.assertEqual(b2.id, 54)

    def test_documentation(self):
        """ test documentation of base model """
        b1 = Rectangle(1, 2)
        self.assertNotEqual(b1.__init__.__doc__, None)
        self.assertNotEqual(b1.width.__doc__, None)
        self.assertNotEqual(b1.height.__doc__, None)
        self.assertNotEqual(b1.x.__doc__, None)
        self.assertNotEqual(b1.y.__doc__, None)
        self.assertNotEqual(b1.area.__doc__, None)
        self.assertNotEqual(b1.display.__doc__, None)
        self.assertNotEqual(b1.update.__doc__, None)
        self.assertNotEqual(b1.to_dictionary.__doc__, None)
        self.assertNotEqual(b1.__str__.__doc__, None)
