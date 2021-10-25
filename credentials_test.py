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

    def test_save_credentials(self):
        '''
        checks if credentials can be saved
        '''
        self.new_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list), 1)

     ###saving multiple credentials###
    def test_saving_multiple_cred(self):
        '''
        method checks whether if users can store multiple credentials
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("Skype", "testuser", "password")
        test_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list), 2)


        ###deleting credentils###
    def test_delete_credentials(self):
        '''
        method tests if one can delete credentials
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("Skype", "testuser", "password")
        test_cred.save_cred()
        self.new_cred.delete_cred()
        self.assertEqual(len(Credentials.cred_list), 1)

     
