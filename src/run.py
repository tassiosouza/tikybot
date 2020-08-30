from tikybot import Tikybot
import time
import random
from fserver import Server

server = Server()

tikybot = Tikybot(server)


current_follow_count = 0
max_follow_count = 600

current_like_count = 0
max_like_count = 300

current_comment_count = 0
max_comment_count = 300

current_watch_count = 0

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


#tikybot.debug_mouse_position()
current_account = 0;

while True:

    account_list = server.get_accounts()
    current_user = account_list[current_account]
    current_login = current_user["credentials"]["username"]
    current_password = current_user["credentials"]["password"]

    if(tikybot.login(current_login, current_password) == False):
        continue


    #tikybot.unfollow(50000)

    #######################################################################################
    # ---------------------------------FOLLOW FOLLOWERS ACTION--------------------------------
    #######################################################################################
    if current_follow_count < max_follow_count:
        follow_delay = random.randrange(3, 5)
        timeout = random.randrange(10 , 50)
        follow_increment = tikybot.follow_user_followers(get_random_famous(), 0, timeout)

    time.sleep(random.randrange(1, 3))
    # ---------------------------------------------------------------------------------------


    #######################################################################################
    #---------------------------------LIKE FOLLOWERS ACTION--------------------------------
    #######################################################################################
    # if current_like_count < max_like_count:
    #     like_delay = random.randrange(2, 4)
    #     timeout = random.randrange(30, 200)
    #     like_increment = tikybot.like_followers_of(get_random_famous(), like_delay, timeout)
    #
    # time.sleep(random.randrange(1, 3))
    #---------------------------------------------------------------------------------------

    #######################################################################################
    # ---------------------------------WATCH FEED ACTION--------------------------------
    #######################################################################################
    # timeout = random.randrange(30, 60)T
    # videos_increment = tikybot.watch_feed_videos(timeout)
    #
    # time.sleep(random.randrange(1, 3))
    # ---------------------------------------------------------------------------------------


    #######################################################################################
    # ---------------------------------COMMENT ON FEED ACTION--------------------------------
    #######################################################################################
    # comment_delay = random.randrange(5, 10)
    # timeout = random.randrange(30, 150)
    # if current_comment_count < max_comment_count:
    #     comment_increment = tikybot.comment_on_feed(["Muito bom !!", "Perfeito :)", "Que lindo !", "kkkkkk", "hahahah",
    #     "Quer saber como conseguir seguidores brasileiros reais ? Acesse nosso perfil e saiba mais"], comment_delay, timeout)
    # ---------------------------------------------------------------------------------------

    #reports
    current_follow_count += follow_increment
    # current_like_count += like_increment
    # current_comment_count += comment_increment
    # current_watch_count += videos_increment

    print("#########################")
    print("Report: ")
    print("Follow count -> " + str(current_follow_count))
    # print("Comment count -> " + str(current_comment_count))
    # print("like count -> " + str(current_like_count))
    # print("Watched videos count -> " + str(current_watch_count))
    print("#########################")

    tikybot.logout()
    time.sleep(3)
    current_account += 1
    if(current_account == 2):
        current_account = 0;

    # if(current_follow_count >= max_follow_count and current_like_count >= max_like_count and
    # current_comment_count >= max_comment_count):
    #     break
#
#
#
# # tikybot.logout()
#
# # while True:
#
# #     tikybot.watch_feed_videos(3)
#
# #tikybot.debug_mouse_position()
# #tikybot.like_by_hashtag("recife")









