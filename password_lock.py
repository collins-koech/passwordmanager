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

def __init__(self,first_name,last_name,password):
  
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def delete_user(self):

        '''
        delete_contact method
        '''
        User.user_list.remove(self)