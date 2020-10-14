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
def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James","Muriuki","asdfgh890") # create contact object
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
def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"James")
        self.assertEqual(self.new_user.last_name,"Muriuki")
        self.assertEqual(self.new_user.password,"asdfgh890")
