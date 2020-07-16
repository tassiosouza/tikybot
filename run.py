from tikybot import Tikybot
import time

tikybot = Tikybot()
tikybot.login("tikybot","")
tikybot.watch_feed_videos(3)
time.sleep(2)
tikybot.follow_user_followers("letlopesoficial", 2)
time.sleep(2)
tikybot.like_by_hashtag("recife")

# while True:

#     tikybot.watch_feed_videos(3)

tikybot.debug_mouse_position()
#tikybot.like_by_hashtag("recife")









