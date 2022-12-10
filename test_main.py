'''

    => Script for liking all the instgram stories of follower of any user <=

    WARNING:- INSTAGRAM MIGHT BLOCK THE SCRIPT IF IT IS USED CONTINUOUSLY. YOU MIGHT
    SOMETIMES SEE A MESSAGE IN THE CONSOLE WHICH TELLS TO ENTER A 6 DIGIT NUMBER WHICH
    THE INSTGRAM WILL SEND YOU ON YOUR EMAIL/PHONE NUMBER. THE PROCESS OF LIKING TAKES
    SOME TIME, YOU WILL NOT SEE IMMEDIATE RESULTS, SO BE PATIENT.

'''

from lib.liker_by_username import start_liker_by_username
from lib.task_info import task_info
from lib.connection import connection

# Main driver function 
def main():

    info = task_info()
    info.log_info()

    conn = connection(info.username, info.password).conn
    
    start_liker_by_username(conn, info)

    print("---> Finished")
    print("")


if __name__ == '__main__':

    try:
        main()

    except Exception as e:
        print(f"Failed: {e}")

    finally:
        input("Press Enter to exit")
