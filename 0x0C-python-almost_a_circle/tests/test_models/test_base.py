#!/usr/bin/python3
""" Unit test for base model file """
import unittest
from models.base import Base


class test_BaseModel(unittest.TestCase):
    """ Tests of the model base"""
    def test_id(self):
        """ Test id to the base model """
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b2 = Base(54)
        self.assertEqual(b2.id, 54)

    def test_documentation(self):
        """ Test documentation of base model """
        b1 = Base()
        self.assertNotEqual(b1.__init__.__doc__, None)
        self.assertNotEqual(b1.__doc__, None)
        self.assertNotEqual(b1.to_json_string.__doc__, None)
        self.assertNotEqual(b1.from_json_string.__doc__, None)
        self.assertNotEqual(b1.save_to_file.__doc__, None)
        self.assertNotEqual(b1.save_to_file_csv.__doc__, None)
        self.assertNotEqual(b1.load_from_file_csv.__doc__, None)
        self.assertNotEqual(b1.create.__doc__, None)
        self.assertNotEqual(b1.load_from_file.__doc__, None)
        self.assertNotEqual(b1.draw.__doc__, None)
