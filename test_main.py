'''


    => Script for liking all the instgram stories of follower of any user <=

    WARNING:- INSTAGRAM MIGHT BLOCK THE SCRIPT IF IT IS USED CONTINUOUSLY. YOU MIGHT
    SOMETIMES SEE A MESSAGE IN THE CONSOLE WHICH TELLS TO ENTER A 6 DIGIT NUMBER WHICH
    THE INSTGRAM WILL SEND YOU ON YOUR EMAIL/PHONE NUMBER. THE PROCESS OF LIKING TAKES
    SOME TIME, YOU WILL NOT SEE IMMEDIATE RESULTS, SO BE PATIENT.


'''

from lib.liker_by_username import liker_by_username
from lib.task_info import task_info

# Main driver function 
def main():

    info = task_info()
    info.log_info()

    try:
    
        # Initialized Insta_Story_Liker instance
        liker =  liker_by_username(
            info.username, 
            info.password, 
            info.target_username, 
            info.no_of_accounts, 
            info.delay
        )

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
