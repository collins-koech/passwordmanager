import pyperclip

class User:
    """
    class that generates new instances of Users
    """
    user_list = []
    def save_user(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        User.user_list.append(self)