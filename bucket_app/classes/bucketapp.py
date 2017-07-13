class BucketApp(object):
    '''Registers and signs up user'''

    def __init__(self):
        self.users_created = []

    def registerUser(self, user):
        '''Registering user accounts and appending them to users_created'''
        self.users_created.append(user)
        print(len(self.users_created))    

    def login(self, loggedin_user):
        '''Checks if loggedin_user exits and login into their account'''
        for user in self.users_created:
            print(user.email)
            print(user.username)
            print(user.firstname)
            if user.email == loggedin_user.email and user.password == loggedin_user.password:
                print(user)
                return user
            