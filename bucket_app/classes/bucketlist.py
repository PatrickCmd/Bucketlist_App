class Bucket(object):
    '''Class to create bucket objects'''

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description
        self.bucketitems = []

    