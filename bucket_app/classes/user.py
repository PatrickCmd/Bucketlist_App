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
    