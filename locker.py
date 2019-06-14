import random
import pyperclip


def all():
    print("Hello, my name is Joshua.I'm here to help you create and save passwords.Do you have an account?(y/n)")
    answer = input()
    if answer == 'n':
        print("Enter your Name")
        username = input()
        print("\n")
        print("Enter A password")
        password = input()
        print("\n")


        handle = open("credentials.txt","a")

        handle.write(username)
        handle.write("")
        handle.write(password)
        handle.write("")
        handle.write(email)
        handle.write("")

        handle.close()
        print("Your Acoount has been created successfully\n Would you like to create new account credentials?(y/n)")
        userresponse = input()
        if userresponse == 'y':
            generate_account()

        else:
            print("Be sure to come back if you would like to use the app again.")

    #    elif answer == 'y':
            login()


def generate_account():
    print()

class User:
    '''
    Class that generates new instances of user_list
    '''
    User_list = []

    def __init__(self, username, password,):

        self.username = username
        self.password = password



    class credentials:
        '''
        Class that generates new instances of credentials
        '''
        User_list = []

    def __init__(self, account, password, ):
        self.account = account
        self.password = password
