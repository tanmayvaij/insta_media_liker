from time import sleep

class liker_by_hashtag:

    # contructor for getting connection and information object
    def __init__(self, conn, info):
        self.conn = conn
        self.info = info

    def like_top_media(self):

        print("---> Starting with liking top media by hashtag")
        print("")

        # Stoping the code for some seconds
        print(f"---> Sleeping for {self.info.delay} seconds")
        print("")        
        sleep(self.info.delay)

        # Top #1 media from hashtag
        top_media_info = self.conn.hashtag_medias_top(self.info.target_hashtag, amount=1)[0]

        print(f"Got media with id:- {top_media_info.id}")
        print("")

        # Liking the post
        res = self.conn.media_like(str(top_media_info.id))

        if res == True:
            print(f"---> ❤️  liked media with id -> {top_media_info.id}") 
            print("")

        else:
            print(f"---> 👎 Failed liking story with id -> {top_media_info.id}")    
            print("")


def start_liker_by_hashtag(conn, info):

    try: 

        # initialized liker_by_hashtag instance
        liker = liker_by_hashtag(conn, info)

        # Liking the top media
        liker.like_top_media()

    except Exception as e:
        print("---> Error Occurred while liking by hashtag")
        print(f"---> Failed: {e}")
        print("")
