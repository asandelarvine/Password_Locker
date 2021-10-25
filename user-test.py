# Importing the unittest module
import unittest 
# Importing the contact class
from user import User
 
class TestUser(unittest.TestCase): 



    def setUp(self):
        """
        setUp method to run before each test cases
        """
        ####new user created####
        self.new_user = User("Larvine", "asande@123")

        def tearDown(self):
            """
            tearDown method cleans up after each test case has run to prevent errors
            """
            User.user_list = []

        def test__init(self):
            """
            test__init checks whether the objects' initialized as it should
            """
            self.assertEqual(self.new_user.username, "Larvine")
            self.assertEqual(self.new_user.password, "asande@123")
