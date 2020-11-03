from tikybot import Tikybot
import time
import random
from fserver import Server

class Session:

    MAX_FOLLOW_COUNT = 200

    current_account = 0

    def __init__(self):
        self.server = Server()
        self.users = self.server.get_accounts()
        self.tikybot = Tikybot(self.server)

    def update_users(self):
        self.users = self.server.get_accounts()

    def run(self):

        while True:
            self.update_users()

            if len(self.users) > 0:

                current_user = self.users[self.current_account]
                if self.verify_user(current_user):

                    if self.session_start(current_user):

                        self.session_follow()
                        self.session_end()
                        self.session_next()

                    else:
                        self.session_next()
                        continue

            else:
                print('Nenhuma conta registrada')

    @staticmethod
    def verify_user(user):
        has_credential = "credentials" in user
        login_failed = user["authState"] == "failed"

        if not has_credential:
            print("User has no credentials")
            return False
        if login_failed:
            print("User has wrong credentials")
            return False

        return True

    def session_end(self):
        
        self.tikybot.logout()

    def session_start(self, user):
        current_login = user["credentials"]["username"]
        current_password = user["credentials"]["password"]
        current_uid = user["uid"]
        return self.tikybot.login(current_login, current_password, current_uid)

    def session_next(self):
        self.current_account += 1
        if (self.current_account >= len(self.users)):
            self.current_account = 0;

    def session_follow(self):

        timeout = random.randrange(30, 100)
        follow_increment = self.tikybot.follow_user_followers(self.get_random_famous(), 0, timeout)
        time.sleep(random.randrange(1, 3))

    def get_random_famous(self):
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




