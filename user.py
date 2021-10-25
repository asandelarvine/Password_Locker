####User Class####
class User:
    """
    Class that generates new instance of User.  
    """
    #list of users to b stored
    user_list = []

    def __init__(self,username,password):
        """
        this method saves the user credentials into user_list  
        """
        self.username = username
        self.password = password

    #####save multiple users#####

    def save_user(self):
        User.user_list.append(self)

    #####delete user#####
    def delete_user(self):
        """
        deletes user account
        """
        User.user_list.remove(self)

        ####find user#####
        @classmethod
        def find_user(cls, username):
            """
            checks if a user exists
            """
            for user in cls.user_list:
                if user.username ==username:
                    return user