from instagrapi import Client

client = Client()

# Taking username and password of the user
# username = input("Enter your username:- ")
# password = input("Enter your password:- ")

try:

    # Login into instagram account
    client.login('tony_bot_224', 'tejomay1234')

    # Get all following users
    # user_following_list = list(map(int, client.user_following(client.user_id).keys()))

    print(client.user_stories(8015684279))

except Exception as e:

    print(f"Failed: {e}")
