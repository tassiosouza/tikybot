from tikybot import Tikybot
import time
import random

tikybot = Tikybot()

comment_delay = random.randrange(3, 5)
tikybot.comment_on_feed(["Muito bom !!", "Quer saber como conseguir seguidores brasileiros reais ? Acesse nosso perfil e saiba mais"], 5, comment_delay)
# tikybot.login("tikybot","")
# tikybot.watch_feed_videos(1)
# time.sleep(1)
# tikybot.follow_user_followers("isisvalverde020", 1)
# time.sleep(1)
# tikybot.like_by_hashtag("recife")
# time.sleep(1)
# tikybot.logout()

# while True:

#     tikybot.watch_feed_videos(3)

#tikybot.debug_mouse_position()
#tikybot.like_by_hashtag("recife")









