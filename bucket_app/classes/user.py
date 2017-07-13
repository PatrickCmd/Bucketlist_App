class User(object):
    '''Class to create user object'''

    def __init__(self, email, password, firstname = None, lastname = None, username = None):
        '''User object constructor to initialise its objects'''
        self.firstname = firstname
        self.lastname  = lastname
        self.username  = username
        self.email     = email
        self.password  = password
        self.id        = None
        self.buckets   = []

    def create_user_bucketlist(self, bucketlist):
        self.buckets.append(bucketlist)
    
    def view_user_bucketlist(self, user):
        pass
    
    def edit_user_bucketlist(self, bucket_name, new_bucket_name, bucket_description):
        '''Editing user buckets'''
        for bucket in self.buckets:
            if bucket.name == bucket_name:
                bucket.name = new_bucket_name
                bucket.description = bucket_description
    
    def delete_user_bucketlist(self, bucket_name):
        '''Delete user bucket'''
        for bucket in self.buckets:
            if bucket.name == bucket_name:
                self.buckets.remove(bucket)
    
    def create_bucketlist_item(self, bucket_name, bucketitem):
        '''creates bucketlist items for the user buckets'''
        for bucket in self.buckets:
            if bucket.name == bucket_name:
                bucket.bucketitems.append(bucketitem)
    
    def edit_bucketlist_item(self, bucketname):
        pass
    
    def delete_bucketlist_item(self, bucketname):
        pass