from tikybot import Tikybot
import time
import random

tikybot = Tikybot()

current_follow_count = 0
max_follow_count = 200

current_comment_count = 0
max_comment_count = 300

def get_random_famous():
    sort = random.randrange(1, 5)
    if sort == 1:
        return ("brunamarquezine")
    elif sort == 2:
        return ("grazimassafer")
    elif sort == 3:
        return ("rkalimann")
    elif sort == 4:
        return ("gabimartinscantora")
    elif sort == 5:
        return ("claudialeitte")

tikybot.login("tikybot", "T#4967163452#t")

while current_comment_count < max_comment_count and current_follow_count < max_follow_count:

    # Perform follow
    follow_increment = random.randrange(3, 5)

    if current_follow_count < max_follow_count:
        follow_delay = random.randrange(3, 5)
        tikybot.follow_user_followers(get_random_famous(), follow_increment, follow_delay)

    time.sleep(random.randrange(5, 8))

    # Watch some videos
    videos_increment = random.randrange(3, 6)
    tikybot.watch_feed_videos(videos_increment)

    time.sleep(random.randrange(5, 8))

    # Perform comment
    comment_increment = random.randrange(6, 9)
    comment_delay = random.randrange(3, 5)
    if current_comment_count < max_comment_count:
        tikybot.comment_on_feed(["Muito bom !!", "Perfeito :)",
        "Quer saber como conseguir seguidores brasileiros reais ? Acesse nosso perfil e saiba mais"], comment_increment, comment_delay)

    current_follow_count += follow_increment
    current_comment_count += comment_increment
    print("#########################")
    print("Report: ")
    print("Follow count -> " + str(current_follow_count))
    print("Comment count -> " + str(current_comment_count))
    print("#########################")



# tikybot.logout()

# while True:

#     tikybot.watch_feed_videos(3)

#tikybot.debug_mouse_position()
#tikybot.like_by_hashtag("recife")









