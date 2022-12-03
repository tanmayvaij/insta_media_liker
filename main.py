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
    def following_list(self):

        return list(map(int, self.client.user_following(self.client.user_id).keys()))

    # Get list of story pks
    def story_pks(self, users_list: list):

        # All story pk emppty list initialized
        all_pks = []

        for user_id in users_list:

            # story pk list of a single user
            single_user_pks = list(map(int, [ i.pk for i in self.client.user_stories(user_id) ]))

            # Combining all story pks
            all_pks += single_user_pks

        return all_pks


if __name__ == '__main__':
    
    liker = Insta_Story_Liker("tony_bot_224", "tejomay1234")
    user_list = liker.following_list()
    print(liker.story_pks(user_list))
