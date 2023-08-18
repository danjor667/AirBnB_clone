#!/usr/bin/python3
'''Definition of test class for `Amenity` class
'''
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    '''TestAmenity: defines tests for `Amenity` objects
    '''

    def test_inherits_BaseModel(self):
        '''Test ensures that `Amenity` objects inherit from BaseModel
        '''
        self.test_amenity = Amenity()
        self.assertIsInstance(self.test_amenity, BaseModel)

    def test_name_exists(self):
        '''Test ensures `Amenity` object has attribute `name`
        '''
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_name_type(self):
        '''Tests ensures `name` is of type str
        '''
        self.assertIsInstance(Amenity.name, str)


if __name__ == "__main__":
    unittest.main()
