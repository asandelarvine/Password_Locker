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

         ###delete credentials###
    def delete_cred(self):
        '''
        method deletes credentials
        '''
        Credentials.cred_list.remove(self)

        ###search for credentials###
    @classmethod
    def find_account(cls,cred_list):
        '''
        method searchs for accounts
        '''
        for cred in cls.cred_list:
            if cred.account == account:
                return cred

             ###confirm credentials###
    @classmethod
    def cred_exists(cls,account):
        '''
        method confirms if a class exists
        '''   
        for cred in cls.cred_list:
            if cred.account == account:
                return True
        return False

        ###display credentials###
    @classmethod
    def display_cred(cls):
        '''
        method that returns all credentials
        '''
        return cls.cred_list


        ###copy password###
    @classmethod
    def copy_passlock(cls, passlock):
        find_account = Credentials.find_account(passlock)
        pyperclip.copy(find_account.passlock)


