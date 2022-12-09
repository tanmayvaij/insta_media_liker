'''


    => Script for liking all the instgram stories of follower of any user <=

    WARNING:- INSTAGRAM MIGHT BLOCK THE SCRIPT IF IT IS USED CONTINUOUSLY. YOU MIGHT
    SOMETIMES SEE A MESSAGE IN THE CONSOLE WHICH TELLS TO ENTER A 6 DIGIT NUMBER WHICH
    THE INSTGRAM WILL SEND YOU ON YOUR EMAIL/PHONE NUMBER. THE PROCESS OF LIKING TAKES
    SOME TIME, YOU WILL NOT SEE IMMEDIATE RESULTS, SO BE PATIENT.


'''

from liker_by_username import liker_by_username

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
        liker =  liker_by_username(username, password, target, accounts, delay)

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
