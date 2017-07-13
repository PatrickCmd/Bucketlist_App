from app import app
import unittest
from classes.bucketapp import BucketApp
from classes.user import User
from classes.bucketlist import Bucket


class CrudTests(unittest.TestCase):
    '''Tests for the crud functionalities of the application'''

    def setUp(self):
        
        # creating testclient for the application
        self.app = app.test_client()
        self.app.testing = True


        self.bucketapp = BucketApp()
        self.user = User('pat@gmail.com', 'pat123')
        self.bucket = Bucket()

    # crud operation tests    
    def test_user_is_created_successfully(self):
        self.bucketapp.registerUser(self.bucketapp)
        self.assertIsInstance(self.bucketapp.users_created, list)
    
    def test_bucket_is_created(self):
        self.assertEqual(len(self.user.buckets) , 0)
        self.user.create_user_bucketlist(self.bucket)
        self.assertEqual(len(self.user.buckets), 1)
    
    def test_bucketlist_item_is_created(self):
        self.assertIsInstance(self.bucket.bucketitems, list)

    # route tests
    def test_home_status_code(self):
        '''sends HTTP GET request to the application on the
        specified'''

        # send request
        result = self.app.get('/')
        # asserting the status code of the response
        self.assertEqual(result.status_code, 200)