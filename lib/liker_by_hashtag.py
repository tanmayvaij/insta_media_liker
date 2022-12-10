from time import sleep


class liker_by_hashtag:


    # contructor for getting connection and information object
    def __init__(self, conn, info):
        self.conn = conn
        self.info = info


    # function for fetching ids of recent media
    def get_recent_hashtag_media(self):

        print(f"---> Fetching all the top {self.info.no_of_posts} recent posts from given hashtag")
        print("")

        # fetched all the top recent posts information in array
        posts_info_arr = self.conn.hashtag_medias_recent(
            self.info.target_hashtag, 
            amount=self.info.no_of_posts
        )

        # getting a list of ids from the post information array
        posts_ids = [ i.id for i in posts_info_arr ]

        print("---> Posts fetched successfully")

        return posts_ids


    def like_recent_media(self, posts_ids: list):

        print("---> Starting with liking recent media by hashtag")
        print("")

        # Stoping the code for some seconds
        print(f"---> Sleeping for {self.info.delay} seconds")
        print("")        
        sleep(self.info.delay)

        # Liking all the posts in loop
        for post_id in posts_ids:
   
            res = self.conn.media_like(post_id)

            if res == True:
                print(f"---> ❤️  liked media with id -> {post_id}") 
                print("")

            else:
                print(f"---> 👎 Failed liking story with id -> {post_id}")    
                print("")

            # Stoping the code for some seconds
            print(f"---> Sleeping for {self.info.delay} seconds")
            print("")        
            sleep(self.info.delay)



def start_liker_by_hashtag(conn, info):

    try: 

        # initialized liker_by_hashtag instance
        liker = liker_by_hashtag(conn, info)

        # fetching the recent media ids
        posts_ids = liker.get_recent_hashtag_media()

        # Liking all the posts
        liker.like_recent_media(posts_ids)

    except Exception as e:
        print("---> Error Occurred while liking by hashtag")
        print(f"---> Failed: {e}")
        print("")
