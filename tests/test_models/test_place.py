#!/usr/bin/python3
'''Defines tests for `Place` class
'''
from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlace(unittest.TestCase):
    '''TestPlace inherits from unittest and tests the `Place` class.
    '''

    def setUp(self):
        '''Defines steps to follow before tests are run
        '''
        self.test_place = Place()

    def test_inherits_basemodel(self):
        '''Tests `Place` inherits from BaseModel
        '''
        self.assertIsInstance(self.test_place, BaseModel)

    def test_cityid_exists(self):
        '''Tests that the `city_id` public class attribute exists
        '''
        self.assertTrue(hasattr(Place, 'city_id'))

    def test_cityid_type(self):
        '''Test ensures `city_id` public class attribute is type str
        '''
        self.assertIsInstance(Place.city_id, str)

    def test_userid_exists(self):
        '''Test ensures `user_id` public class attribute exists
        '''
        self.assertTrue(hasattr(Place, 'user_id'))

    def test_userid_type(self):
        '''Test ensures `user_id` public class attribute is type str
        '''
        self.assertIsInstance(Place.user_id, str)

    def test_name_exists(self):
        '''Test ensures `name` public class attribute exists
        '''
        self.assertTrue(hasattr(Place, 'name'))

    def test_name_type(self):
        '''Test ensures `name` public class attribute is type str
        '''
        self.assertIsInstance(Place.name, str)

    def test_description_exists(self):
        '''Test ensures `description` public class attribute exists
        '''
        self.assertTrue(hasattr(Place, 'description'))

    def test_description_type(self):
        '''Test ensures `description` public class attribute is type str
        '''
        self.assertIsInstance(Place.description, str)

    def test_number_rooms_exists(self):
        '''Test ensures `number_rooms` public class attribute exists
        '''
        self.assertTrue(hasattr(Place, 'number_rooms'))

    def test_number_rooms_type(self):
        '''Test ensures `number_rooms` public class attribute is type int
        '''
        self.assertIsInstance(Place.number_rooms, int)

    def test_number_bathrooms_exists(self):
        '''Test ensures `number_bathrooms` public class attribute exists
        '''
        self.assertTrue(hasattr(Place, 'number_bathrooms'))

    def test_number_bathrooms_type(self):
        '''Test ensures `number_bathrooms` public class attribute is type int
        '''
        self.assertIsInstance(Place.number_bathrooms, int)

    def test_max_guest_exists(self):
        '''Test ensures `max_guest` public class attribute exists
        '''
        self.assertTrue(hasattr(Place, 'max_guest'))

    def test_max_guest_type(self):
        '''Test ensures `max_guest` public class attribute is type int
        '''
        self.assertIsInstance(Place.max_guest, int)

    def test_price_by_night_exists(self):
        '''Test ensures `price_by_night` public class attribute exists
        '''
        self.assertTrue(hasattr(Place, 'price_by_night'))

    def test_price_by_night_type(self):
        '''Test ensures `price_by_night` public class attribute is type int
        '''
        self.assertIsInstance(Place.price_by_night, int)

    def test_latitude_exists(self):
        '''Test ensures `latitude` public class attribute exists
        '''
        self.assertTrue(hasattr(Place, 'latitude'))

    def test_latitude_type(self):
        '''Test ensures `latitude` public class attribute is type float
        '''
        self.assertIsInstance(Place.latitude, float)

    def test_longitude_exists(self):
        '''Test ensures `longitude` public class attribute exists
        '''
        self.assertTrue(hasattr(Place, 'longitude'))

    def test_longitude_type(self):
        '''Test ensures `longitude` public class attribute is type float
        '''
        self.assertIsInstance(Place.longitude, float)

    def test_amenity_ids_exists(self):
        '''Test ensures `amenity_ids` public class attribute exists
        '''
        self.assertTrue(hasattr(Place, 'amenity_ids'))

    def test_amenity_ids_type(self):
        '''Test ensures `amenity_ids` public class attribute is type list
        '''
        self.assertIsInstance(Place.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
