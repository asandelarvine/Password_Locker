import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):
    '''
    Tests class that defines test casesfor the credential class behaviours
    '''

    def setUp(self):
        '''
        method setUp to run before each test cases
        '''
        self.new_cred = Credentials ("GitHub", "larvineasande@gmail.com", "asande@123")

    def tearDown(self):
        '''
        method cleans up b4 anytest is carried out
        '''
        Credentials.cred_list = []

        ###checks initialization###

    def test_init(self):
        '''
        Checks if the object is initialized properly
        '''
        self.assertEqual(self.new_cred.account, "GitHub")
        self.assertEqual(self.new_cred.email, "larvineasande@gmail.com")
        self.assertEqual(self.new_cred.passlock, "asande@123")
