from instagrapi import Client

class Insta_Story_Liker:

    def __init__(self, username: str, password: str):

        # Created instance of instgrapi client
        self.client = Client()

        # Login into instagram account
        print("---> Logging into your account")
        self.client.login(username, password)
        print("---> Logged in successfully")

    # Get all following users
    def following_list(self):

        return list(map(int, self.client.user_following(self.client.user_id).keys()))

    # Get list of story ids
    def story_ids(self, users_list: list):

        # All story pk emppty list initialized
        all_ids = []

        for user_id in users_list:

            # story id list of a single user
            single_user_ids = [ i.id for i in self.client.user_stories(user_id) ]

            # Combining all story ids
            all_ids += single_user_ids

        # Logging all the fetched story ids
        print("Got stories with the follwowing ids:- ")
        for id in all_ids:
            print(f"---> {id}")

        return all_ids

    # Method for liking stories
    def like_stories(self, id_list: list):
        
        for i in id_list:
            self.client.story_like(i)


if __name__ == '__main__':

    try:
    
        liker = Insta_Story_Liker("tony_bot_224", "tejomay1234")
        users_list = liker.following_list()
        all_story_ids = liker.story_ids(users_list)
        # liker.like_stories(all_story_ids)
        print("Finished")

    except Exception as e:

        print(f"Failed: {e}")
