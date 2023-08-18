#!/usr/bin/python3
'''Tests the code definition of the 'City' class.
'''
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    ''''TestCity' class. Tests the definition of the 'City' class.
    '''
    def setUp(self):
        '''sets up the variables for use in later tests.
        '''
        self.city1 = City()
        self.city1.save()

    def test_inherit_BaseModel(self):
        '''Tests if the instance of 'City' class inherits from 'BaseModel'
        '''
        self.assertIsInstance(self.city1, BaseModel)

    def test_hasattr_name(self):
        '''Tests that the 'City' class has a 'name' class attribute
        '''
        self.assertTrue(hasattr(City, "name"))

    def test_name_type(self):
        '''Tests the type of the 'name' class attribute.
        '''
        self.assertIsInstance(City.name, str)

    def test_hasattr_state_id(self):
        '''Tests that the 'City' class has 'state_id' class attribute
        '''
        self.assertTrue(hasattr(City, "state_id"))

    def test_state_id_type(self):
        '''Tests the type of the 'state_id' class attribute.
        '''
        self.assertIsInstance(City.state_id, str)


if __name__ == '__main__':
    unittest.main()
