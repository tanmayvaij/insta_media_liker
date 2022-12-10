from time import sleep

class liker_by_username:

    """
        A class for liking the stories of the followers of the target account 
        given by  the user of this application
    """

    # Class Contructor for getting connection and information object
    def __init__(self, conn, info):
        self.conn = conn
        self.info = info


    # Get all follower users
    def follower_list(self):

        print("---> Fetching follower list, be patient")
        print("")

        # Grabbing user id of target user
        target_user_id = self.conn.user_id_from_username(self.info.target_username)

        # return list of follower's user id
        flist = list(map(  
            int, 
            self.conn.user_followers( 
                target_user_id, 
                amount=self.info.no_of_accounts
            ).keys()
        ))

        print(f"---> Fetched all followers of account - {self.info.target_username}")
        print("")

        print(f"---> Sleeping for {self.info.delay} seconds")
        print("")

        # Stoping the code for some seconds
        sleep(self.info.delay)

        return flist 


    # Get list of story ids
    def get_story_ids_and_like(self, users_list: list):

        # Counter for keeping track on how many accounts have been traversed
        acc_counter = 1

        # Counter Keeping track on how many stories have been liked
        like_count = 0

        for user_id in users_list:

            print(f"---> {acc_counter}. 😐 Trying to fetch stories of user with user id -> {user_id}")

            # story id list of a single user
            story_ids = [ i.id for i in self.conn.user_stories(user_id) ]

            if story_ids != []:

                print(f"---> {acc_counter}. 🤩 Got stories of user with user id -> {user_id}")
                print("")

                res = self.conn.story_like(story_ids[0])

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
            print(f"---> Sleeping for {self.info.delay} seconds")
            print("")

            sleep(self.info.delay)

            acc_counter += 1



def start_liker_by_username(conn, info):

    try:

        # Initialized liker_by_username instance
        liker = liker_by_username(conn, info)

        # Got all the following users list
        users_list = liker.follower_list()

        # Got story ids of all the follwing users having stories and like them
        liker.get_story_ids_and_like(users_list)

    except Exception as e:
        print("---> Error Occurred while liking by username")
        print(f"---> Failed: {e}")
        print("")
