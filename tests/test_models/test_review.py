#!/usr/bin/python3
'''Defines tests for the `Review` class
'''
from models.review import Review
from models.base_model import BaseModel
import unittest


class TestReview(unittest.TestCase):
    '''TestReview class defines tests for `Review` class
    '''

    def test_inherits_BaseModel(self):
        '''Test ensures `Review` inherits from BaseModel
        '''
        self.test_review = Review()
        self.assertIsInstance(self.test_review, BaseModel)

    def test_place_id_exists(self):
        '''Test ensures `place_id` exists in `Review` class
        '''
        self.assertTrue(hasattr(Review, 'place_id'))

    def test_place_id_type(self):
        '''Test ensures `place_id` is of type str
        '''
        self.assertIsInstance(Review.place_id, str)

    def test_user_id_exists(self):
        '''Test ensures `user_id` exists in `Review` class
        '''
        self.assertTrue(hasattr(Review, 'user_id'))

    def test_user_id_type(self):
        '''Test ensures `user_id` is of type str
        '''
        self.assertIsInstance(Review.user_id, str)

    def test_text_exists(self):
        '''Test ensures `text` exists in `Review` class
        '''
        self.assertTrue(hasattr(Review, 'text'))

    def test_text_type(self):
        '''Test ensures `text` is of type str
        '''
        self.assertIsInstance(Review.text, str)


if __name__ == "__main__":
    unittest.main()
