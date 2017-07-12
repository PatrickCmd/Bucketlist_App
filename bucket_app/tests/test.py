import unittest
from classes.bucketapp import BucketApp
from classes.user import User
from classes.bucketlist import Bucket


class CrudTests(unittest.TestCase):
    '''Tests for the crud functionalities of the application'''

    def setUp(self):
        self.bucketapp = BucketApp()
        self.user = User('pat@gmail.com', 'pat123')
        self.bucket = Bucket()

    def test_user_is_created_successfully(self):
        self.bucketapp.registerUser(self.bucketapp)
        self.assertIsInstance(self.bucketapp.users_created, list)
    
    def test_bucket_is_created(self):
        self.assertIsInstance(self.user.buckets, list)
    
    def test_bucketlist_item_is_created(self):
        self.assertIsInstance(self.bucket.bucketitems, list)