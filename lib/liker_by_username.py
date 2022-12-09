from instagrapi import Client
from time import sleep

class liker_by_username:

    # Class Contructor
    def __init__(self, username: str, password: str, target: str, no_of_accounts: int, delay: int):

        # Set target profile
        self.target = target

        # Set number of accounts to scrap
        self.no_of_accounts = no_of_accounts

        # Set delay in each steps
        self.delay = delay

        # Created instance of instgrapi client
        self.client = Client()

        print("---> Logging into your account")

        # Login into instagram account
        self.client.login(username, password)

        print("---> Logged in successfully")


    # Get all follower users
    def follower_list(self):

        print("---> Fetching follower list, be patient")

        # Grabbing user id of target user
        target_user_id = self.client.user_id_from_username(self.target)

        # return list of follower's user id
        flist = list(map(  
            int, 
            self.client.user_followers( 
                target_user_id, 
                amount=self.no_of_accounts
            ).keys()
        ))

        print(f"---> Fetched all followers of account - {self.target}")

        print(f"---> Sleeping for {self.delay} seconds")

        # Stoping the code for some seconds
        sleep(self.delay)

        return flist 


    # Get list of story ids
    def get_story_ids_and_like(self, users_list: list):

        print("---> Fetching story ids")

        # Counter for keeping track on how many accounts have been traversed
        acc_counter = 1

        # Counter Keeping track on how many stories have been liked
        like_count = 0

        for user_id in users_list:

            print(f"---> {acc_counter}. 😐 Trying to fetch stories of user with user id -> {user_id}")

            # story id list of a single user
            story_ids = [ i.id for i in self.client.user_stories(user_id) ]

            if story_ids != []:

                print(f"---> {acc_counter}. 🤩 Got stories of user with user id -> {user_id}")
                print("")

                res = self.client.story_like(story_ids[0])

                if res == True:

                    print(f"---> ❤️  liked story with id -> {story_ids[0]}") 

                    like_count += 1

                else:

                    print(f"---> 👎 Failed liking story with id -> {story_ids[0]}")    

                print("")

            else:

                print(f"---> {acc_counter}. 😥 No stories with user with user id -> {user_id}")
                print("")

            # Stoping the code for some seconds
            print(f"---> Sleeping for {self.delay} seconds")
            print("")

            sleep(self.delay)

            acc_counter += 1
