import unittest  # Importing the unittest module
from Password_Lock import User # Importing the contact class


class TestUser(unittest.TestCase):
  
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James","Muriuki","asdfgh890") # create contact object
def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []