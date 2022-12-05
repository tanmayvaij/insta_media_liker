'''


    => Script for liking all the instgram stories of follower of any user <=

    WARNING:- INSTAGRAM MIGHT BLOCK THE SCRIPT IF IT IS USED CONTINUOUSLY. YOU MIGHT
    SOMETIMES SEE A MESSAGE IN THE CONSOLE WHICH TELLS TO ENTER A 6 DIGIT NUMBER WHICH
    THE INSTGRAM WILL SEND YOU ON YOUR EMAIL/PHONE NUMBER. THE PROCESS OF LIKING TAKES
    SOME TIME, YOU WILL NOT SEE IMMEDIATE RESULTS, SO BE PATIENT.


'''

from instagrapi import Client
from time import sleep

class Insta_Story_Liker:

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

            sleep(self.delay)

            acc_counter += 1



# Main driver function 
def main():

    username = input("Enter your username:- ")

    password = input("Enter your password:- ")

    target = input("Enter target username:- ")

    accounts = int(input("Enter no of accounts to target:- "))

    delay = int(input("Enter the delay:- "))

    if ( username == "" or password == "" or target == "" ) :
        print("---> Missing details")
        print("---> Exiting")
        return

    if accounts == "":
        accounts = 50

    if delay == "":
        delay = 5

    try:
    
        # Initialized Insta_Story_Liker instance
        liker = Insta_Story_Liker(username, password, target, accounts, delay)

        # Got all the following users list
        users_list = liker.follower_list()

        # Got story ids of all the follwing users having stories and like them
        liker.get_story_ids_and_like(users_list)

        print("---> Finished")

    except Exception as e:

        print(f"Failed: {e}")


if __name__ == '__main__':

    main()

    input("Press Enter to exit")
