from instagrapi import Client

class connection:

    def __init__(self, username: str, password: str):
        
        self.conn = Client()

        print("---> Trying to login into your account")

        self.conn.login(username, password)

        print("---> Logged in successfully")
        print("")

