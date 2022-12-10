from instagrapi import Client

class connection:

    """
        A class for a common connection in the whole application
    """

    def __init__(self, username: str, password: str):
        
        # Initialized client instance of instagrapi
        self.conn = Client()

        print("---> Trying to login into your account")

        # Trying the login into your account 
        self.conn.login(username, password)

        print("---> Logged in successfully")
        print("")
