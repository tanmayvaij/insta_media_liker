'''

    => Script for liking all the instgram stories of follower of any user <=

    WARNING:- INSTAGRAM MIGHT BLOCK THE SCRIPT IF IT IS USED CONTINUOUSLY. YOU MIGHT
    SOMETIMES SEE A MESSAGE IN THE CONSOLE WHICH TELLS TO ENTER A 6 DIGIT NUMBER WHICH
    THE INSTGRAM WILL SEND YOU ON YOUR EMAIL/PHONE NUMBER. THE PROCESS OF LIKING TAKES
    SOME TIME, YOU WILL NOT SEE IMMEDIATE RESULTS, SO BE PATIENT.

'''

from lib.task_info import task_info
from lib.connection import connection
from lib.liker_by_username import start_liker_by_username
from lib.liker_by_hashtag import start_liker_by_hashtag


# Main driver function 
def main():

    # task_info instance for collecting, logging the information from user
    info = task_info()
    info.log_info()

    # created one connection with instagram api for liking stories
    print("Creating first connection for liking stories")
    print("")
    conn1 = connection(info.username, info.password).conn

    # created one connection with instagram api for liking posts
    print("Creating second connection for liking posts")
    print("")
    conn2 = connection(info.username, info.password).conn
    
    # calling liker by username if username is given
    if info.target_username_exists:
        start_liker_by_username(conn1, info)

    # calling liker by hashtag if hashtag is given
    if info.target_hashtag_exists:
        start_liker_by_hashtag(conn2, info)

    print("---> Finished")
    print("")


if __name__ == '__main__':

    try:
        main()

    except Exception as e:
        print(f"Failed: {e}")
