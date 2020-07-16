from tikybot import Tikybot
import time

tikybot = Tikybot()
tikybot.login("tikybot","")
tikybot.watch_feed_videos(1)
time.sleep(1)
tikybot.follow_user_followers("isisvalverde020", 1)
time.sleep(1)
tikybot.like_by_hashtag("recife")
time.sleep(1)
tikybot.logout()

# while True:

#     tikybot.watch_feed_videos(3)

#tikybot.debug_mouse_position()
#tikybot.like_by_hashtag("recife")









