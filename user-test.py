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

        def test_save_user(self):
            """
            test_save_user confirms if the users details are saved into the user list
            """
            self.new_user.save_user()
            self.assertEqual(len(User.user_list),1)

        def test_save_multiple_users(self):
            """
            checks if one can store more than one user 
            """
            self.new_user.save_user()
            test_user = User("test", "password")
            test_user.save_user()
            self.assertEqual(len(User.user_list), 2)

        def test_delete_user(self):
            """
            checks whether one can delete a user account
            """
            self.new_user.save_user()
            test_user = User("test","password")
            test_user.save_user()
            self.new_user.delete_user()
            self.assertEqual(len(User.user_list), 1)

        def test_find_user(self):
            """
            checks if one can find a user by username and display its info
            """
            self.new_user.save_user()
            test_user = User("test","password")
            test_user.save_user()
            found_user = User.find_user("Larvine")
            self.assertEqual(found_user.username, self.new_user.username)

    if __name__ == '__main__':
        unittest.main()


                
    
