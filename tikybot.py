from uicontrol import UiControl
import coordinates
import time
import random

from PIL import Image

#Those values depends on screen resolution and emulator position

#Captcha verification
CAPTCHA_MIN_X = 160
CAPTCHA_MAX_X = 338
CAPTCHA_MIN_Y = 360
CAPTCHA_MAX_Y = 505
INITIAL_MOUSE_POSITION_X = 109
INITIAL_MOUSE_POSITION_Y = 432
MOUSE_MOVE_SPEED = 2

#Screen elements positions
MOUSE_FIRST_SEARCH_USER_X = 90
MOUSE_FIRST_SEARCH_USER_Y = 225

REGION_X_OFFSET = 290
REGION_Y_OFFSET_USERID = 7
REGION_Y_OFFSET_USERNAME = 11
REGION_WIDTH = 250
REGION_HEIGHT = 24

#Buttons
BUTTON_HOME = "res/home_button.png"
BUTTON_ADD_ACCOUNT = "res/add_account_button.png"
BUTTON_CAPTCHA_REFRESH = "res/refresh_captcha.png"
BUTTON_LOGOUT = "res/logout_button.png"
BUTTON_FOLLOW = "res/follow_button.png"

class Tikybot():

    def __init__(self, x=0):
        self.x = x
        self.ui_control = UiControl()
        self.ui_control.focus()

    def login(self, username, password):

        print("Performing login for account " + username + "...")

        self.ui_control.click_on_position(coordinates.PROFILE_BUTTON)
        self.ui_control.click_on_position(coordinates.SIGNUP_BUTTON)
        self.ui_control.click_on_image_file(BUTTON_ADD_ACCOUNT)
        self.ui_control.click_on_position(coordinates.USERNAME_BUTTON)
        self.ui_control.click_on_position(coordinates.EMAIL_BUTTON)

        self.ui_control.write(username)
        self.ui_control.press_enter()
        self.ui_control.write(password)

        self.ui_control.click_on_position(coordinates.LOGIN_BUTTON)
        time.sleep(2)

        #verify login
        home_button = self.ui_control.find_image(BUTTON_HOME)

        if home_button is not None:
            print("Successfully logged in")
            return True

        return self.bypass_verification()

    def bypass_verification(self, attempts_number=3):

        print("Performing bypass captcha verification...")

        current_attempt = 0
        while current_attempt < attempts_number:
            print("Attempt: " + str(current_attempt + 1))

            for x in range(1, 11):
                puzzle_name = "res/puzzle" + str(x) + ".png"
                result = self.ui_control.find_image(puzzle_name, confidence=0.6)

                if result is not None and CAPTCHA_MIN_X < result.left < CAPTCHA_MAX_X\
                        and CAPTCHA_MIN_Y < result.top < CAPTCHA_MAX_Y:
                    self.ui_control.drag_and_drop(INITIAL_MOUSE_POSITION_X, INITIAL_MOUSE_POSITION_Y,
                                                  result.left, INITIAL_MOUSE_POSITION_Y)
                    print("Successfully logged in")
                    return True

            self.ui_control.click_on_image_file(BUTTON_CAPTCHA_REFRESH)
            current_attempt += 1

        return False

    def logout(self):

        print("Performing logout...")
        self.ui_control.click_on_position(coordinates.PROFILE_BUTTON)
        self.ui_control.click_on_position(coordinates.OPTION_BUTTON)
        self.ui_control.scroll_for_click(BUTTON_LOGOUT)
        self.ui_control.click_on_position(coordinates.LOGOUT_BUTTON)

    def debug_mouse_position(self):
        self.ui_control.debug_mouse_position()

    def follow_user_followers(self, username, amount):

        print("Performing following followers...")

        self.ui_control.click_on_position(coordinates.DISCOVER_BUTTON)
        self.ui_control.click_on_position(coordinates.SEARCH_BAR)
        self.ui_control.write(username)
        self.ui_control.click_on_position(coordinates.SEARCH_BUTTON)

        time.sleep(3)
        self.ui_control.click_on_position(coordinates.FIRST_USER_IN_LIST)
        self.ui_control.click_on_position(coordinates.FOLLOWERS_BUTTON)
        time.sleep(2)

        current_follow_count = 0
        while current_follow_count < amount:
            success = self.ui_control.scroll_for_find(BUTTON_FOLLOW)
            if success:
                #Get userid
                userid_region = (success.left - REGION_X_OFFSET, success.top - REGION_Y_OFFSET_USERID, REGION_WIDTH, REGION_HEIGHT)
                userid = self.ui_control.read_text_in_region(userid_region)
                print("username - " + userid)
                #get username
                username_region = (success.left - REGION_X_OFFSET, success.top + REGION_Y_OFFSET_USERNAME, REGION_WIDTH, REGION_HEIGHT)
                username = self.ui_control.read_text_in_region(username_region)
                print("name - " + username)

                if(username is not None and userid is not None):
                    self.ui_control.click_on_image(success)
                    current_follow_count += 1

        self.ui_control.click_on_position(coordinates.TOP_BACK_BUTTON)
        self.ui_control.click_on_position(coordinates.TOP_BACK_BUTTON)
        self.ui_control.click_on_position(coordinates.TOP_BACK_BUTTON)
        self.ui_control.click_on_position(coordinates.HOME_BUTTON)

    def watch_feed_videos(self, amount):
        current_count = 0
        while current_count < amount:
            self.ui_control.scroll_screen_up(10)
            time.sleep(random.randrange(15,20))
            current_count += 1

    def like_by_hashtag(self, hashtag):

        print("Performing like by hashtag >>" + hashtag + "<< ...")

        self.ui_control.click_on_position(coordinates.DISCOVER_BUTTON)
        self.ui_control.click_on_position(coordinates.SEARCH_BAR)
        self.ui_control.write("#" + hashtag)
        self.ui_control.click_on_position(coordinates.SEARCH_BUTTON)

        time.sleep(2)
        self.ui_control.click_on_position(coordinates.FIRST_HASHTAG_IN_LIST)
        self.ui_control.click_on_position(coordinates.FIRST_VIDEO_IN_HASGTAG_RESULT)
        #DO LIKE AND RETRIEVE USER
        self.ui_control.click_on_position(coordinates.TOP_BACK_BUTTON)
        self.ui_control.click_on_position(coordinates.SECOND_VIDEO_IN_HASGTAG_RESULT)
        # DO LIKE AND RETRIEVE USER
        self.ui_control.click_on_position(coordinates.TOP_BACK_BUTTON)
        self.ui_control.click_on_position(coordinates.THIRD_VIDEO_IN_HASGTAG_RESULT)
        self.ui_control.click_on_position(coordinates.TOP_BACK_BUTTON)

        self.ui_control.click_on_position(coordinates.TOP_BACK_BUTTON)
        self.ui_control.click_on_position(coordinates.TOP_BACK_BUTTON)
        self.ui_control.click_on_position(coordinates.HOME_BUTTON)