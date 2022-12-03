from instagrapi import Client

class Insta_Story_Liker:

    def __init__(self, username, password):

        # Created instance of instgrapi client
        self.client = Client()

        # Login into instagram account
        try:
            self.client.login(username, password)
        except Exception as e:
            print(f"Failed: {e}")

    def get_following_list(self):

        # Get all following users
        return list(map(int, self.client.user_following(self.client.user_id).keys()))