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

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)

def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","asdfgh890",) # new contact
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
  # setup and class creation up here

# other test cases here
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","asdfgh890",) # new contact
            test_user.save_user()

            self.new_user.delete_user()# Deleting a contact object
            self.assertEqual(len(User.user_list),1)

def test_find_user_by_password(self):
        '''
        test to check if we can find a user by phone password and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","asdfgh8901",) # new contact
        test_user.save_user()

        found_user = User.find_by_password("asdfgh8901")

        self.assertEqual(found_user.first_name,test_user.first_name)
def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_user.save_user()
        test_user = User("Test","user","asdfgh8901",) # new contact
        test_user.save_user()

        user_exists = User.user_exist("asdfgh8901")

        self.assertTrue(user_exists)