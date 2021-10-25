import pyperclip
class Credentials:
    '''
    Class that generates new instances of user's credentials
    '''
    cred_list = []

    ###assigning property to credential list###
    def __init__(self, account, email, passlock):

        self.account = account
        self.email = email
        self.passlock = passlock

        ###save credentials###
    def save_cred(self):
        '''
        method saves credentials objects into the cred_list
        '''
        Credentials.cred_list.append(self)
