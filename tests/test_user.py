import unittest
from .models import User 

class UserModelTest(unittest,TestCase):
     '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_user = User(password = 'mosoti')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verify(self):
        self.assertTrue(self.new_user.verify_password('mosoti'))

if __name__ == '__main__':
    unittest.main()




    