#!/usr/bin/python3
'''Test file for the 'State' class definition.
'''
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    ''''TestState' class. Used to test the definition of the 'State' class.
    '''
    def setUp(self):
        '''Sets up variables for use in later parts of the test.
        '''
        self.state1 = State()
        self.state1.save()

    def test_inherit_from_BaseModel(self):
        '''Test if the instance of class 'State' inherits from 'BaseModel'
        '''
        self.assertIsInstance(self.state1, BaseModel)

    def test_hasattr_name(self):
        '''Test if the 'State' class has the 'name' class attribute
        '''
        self.assertTrue(hasattr(State, "name"))

    def test_name_type(self):
        '''Tests the type of the 'name' class attribute
        '''
        self.assertIsInstance(State.name, str)


if __name__ == '__main__':
    unittest.main()
