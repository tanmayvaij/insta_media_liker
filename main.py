from instagrapi import Client

class Insta_Story_Liker:

    def __init__(self, username: str, password: str):

        # Created instance of instgrapi client
        self.client = Client()

        # Login into instagram account
        try:
            self.client.login(username, password)
        except Exception as e:
            print(f"Failed: {e}")

    # Get all following users
    def get_following_list(self):

        return list(map(int, self.client.user_following(self.client.user_id).keys()))

if __name__ == '__main__':
    
    liker = Insta_Story_Liker("tony_bot_224", "tejomay1234")
    print(liker.get_following_list())
