from instagrapi import Client

class connection:

    def __init__(self, username: str, password: str):
        
        self.conn = Client()
        self.conn.login(username, password)

