'''


    => Script for liking all the instgram stories of follower of any user <=

    WARNING:- INSTAGRAM MIGHT BLOCK THE SCRIPT IF IT IS USED CONTINUOUSLY. YOU MIGHT
    SOMETIMES SEE A MESSAGE IN THE CONSOLE WHICH TELLS TO ENTER A 6 DIGIT NUMBER WHICH
    THE INSTGRAM WILL SEND YOU ON YOUR EMAIL/PHONE NUMBER. THE PROCESS OF LIKING TAKES
    SOME TIME, YOU WILL NOT SEE IMMEDIATE RESULTS, SO BE PATIENT.


'''

from instagrapi import Client

class Insta_Story_Liker:

    # Class Contructor
    def __init__(self, username: str, password: str, target: str):

        # Set target profile
        self.target = target

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
        flist = list(map(int, self.client.user_followers(target_user_id, amount=50).keys()))

        print(f"---> Fetched all followers of account - {self.target}")

        return flist 


    # Get list of story ids
    def story_ids(self, users_list: list):

        print("---> Fetching story ids")

        # All story pk empty list initialized
        all_ids = []

        # Counter for keeping track on how many accounts have been traversed
        acc_counter = 1

        for user_id in users_list:

            print(f"---> {acc_counter}. 😐 Trying to fetch stories of user with user id -> {user_id}")

            # story id list of a single user
            single_user_ids = [ i.id for i in self.client.user_stories(user_id) ]

            # Combining all story ids
            if single_user_ids != []:

                all_ids += single_user_ids

                print(f"---> {acc_counter}. 🤩 Got stories of user with user id -> {user_id}")

            else:

                print(f"---> {acc_counter}. 😥 No stories with user od user id -> {user_id}")

            acc_counter += 1

            # Stop collecting ids if fetched ids are more than 50
            if len(all_ids) > 50:

                print("---> Finished fetching stories")

                break
        
        print(f"Got {len(all_ids)} stories with the ids:- ")

        # Logging all the fetched story ids
        for id in all_ids:
            print(f"---> {id}")

        return all_ids


    # Method for liking stories
    def like_stories(self, id_list: list):
        
        print("---> Starting liking process")

        for i in id_list:

            res = self.client.story_like(i)

            if res == True:

                print(f"---> liked story with id -> {i}") 

            else:

                print(f"---> Failed liking story with id -> {i}")      



# Main driver function 
def main():

    username = input("Enter your username:- ")

    password = input("Enter your password:- ")

    target = input("Enter target username:- ")

    try:
    
        # Initialized Insta_Story_Liker instance
        liker = Insta_Story_Liker(username, password, target)

        # Got all the following users list
        users_list = liker.follower_list()

        # Got story ids of all the follwing users having stories
        all_story_ids = liker.story_ids(users_list)

        # Liked all the stories
        # liker.like_stories(all_story_ids)

        print("---> Finished")

    except Exception as e:

        print(f"Failed: {e}")


if __name__ == '__main__':

    main()
