class task_info:


    # Getting all information from the user
    def __init__(self):

        # Taking inputs
        self.username = input("Enter your username:- ")
        self.password = input("Enter your password:- ")
        self.target_username = input("Enter target username:- ")
        self.target_hashtag = input("Enter target hastag:- ")
        self.no_of_accounts = input("Enter no of accounts to target (default: 50):- ")
        self.delay = input("Enter the delay: (default: 5)- ")
        print("")

        # Check if some target username exists or not
        if self.target_username != "":
            self.target_username_exists = True
        else:
            self.target_username_exists = False

        # Check if some target hashtag exists or not
        if self.target_hashtag != "":
            self.target_hashtag_exists = True
        else:
            self.target_hashtag_exists = False

        # Checking if username password entered or not, if not entered the exiting the code
        if self.username == "" or self.password == "":
            print("---> Missing details, Restart the script and try again")
            print("---> Exiting")
            exit()

        # If no. of accounts not set, then setting it to 50 by default
        if self.no_of_accounts == "":
            self.no_of_accounts = 50
        else:
            self.no_of_accounts = int(self.no_of_accounts)

        # If delay in each step not set, then setting it to 5 by default
        if self.delay == "":
            self.delay = 5
        else:
            self.delay = int(self.delay)

        print("---> 😎 Thanks for the information ")
        print("")


    # Logging all the details entered by user
    def log_info(self):

        print("---> Entered details can be seen below")
        print(f"---> username:- {self.username}")
        print(f"---> password:- {self.password}")
        print(f"---> target username:- {self.target_username}")
        print(f"---> target hashtag:- {self.target_hashtag}")
        print(f"---> No of accounts to scrap:- {self.no_of_accounts}")
        print(f"---> Deplay in each step:- {self.delay}")
        print("")
