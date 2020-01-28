#!/usr/bin/python3
""" Unit test for base model file """
import unittest
from models.base import Base

class TestBaseModel(unittest.TestCase):
    """ Tests of the model base"""
    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
