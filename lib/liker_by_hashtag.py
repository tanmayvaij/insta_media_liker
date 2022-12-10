from time import sleep

class liker_by_hashtag:

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
        top_media = self.conn.hashtag_medias_top(self.info.target_hashtag, amount=1)[0].dict()

        # Got id of the top most media
        media_id = top_media.id

        res = self.conn.media_like(media_id)

        if res == True:
            print(f"---> ❤️  liked media with id -> {media_id}") 
            print("")

        else:
            print(f"---> 👎 Failed liking story with id -> {media_id}")    
            print("")


def start_liker_by_hashtag(conn, info):

    # initialized liker_by_hashtag instance
    liker = liker_by_hashtag(conn, info)

    # Liking the top media
    liker.like_top_media()
