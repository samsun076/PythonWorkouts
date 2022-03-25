"""
Create a dict in which the keys are usernames and the values are passwords, both represented as strings. 
Create a tiny login system, in which the user must enter a username and password. 
If there is a match, then indicate that the user has successfully logged in. 
If not, then refuse them entry. (Note: This is a nice little exercise, but please never store unencrypted passwords. It’s a major secu- rity risk.)
"""


USERS = {'dm': 'password', 
          'lb': 'pickles'}


def login():
    while True: 
        username = input("Enter user: ").strip()
        password = input("Enter Password: ").strip()
        if USERS.get(username) == password:
            print(f'Welcome {username}!')
            break
        else:
            print("try again")
            continue
login()

