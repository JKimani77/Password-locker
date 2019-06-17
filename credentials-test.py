import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):

    '''
    test class that defines test cases for  the credentials class
    '''

    def setUp(self):
        '''
        set up method  that runs before each test case
        '''

        self.new_credentials = Credentials("Google", "3344")

    def tearDown(self):
        '''
         tear down method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
