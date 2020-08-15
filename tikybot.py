from uicontrol import UiControl
import constants
import time
import random
from datetime import datetime

class Tikybot():

    def __init__(self, x=0):
        self.x = x
        self.ui_control = UiControl()
        self.ui_control.focus(constants.INITIAL_MOUSE_POSITION_X, constants.INITIAL_MOUSE_POSITION_Y)

    def login(self, username, password):

        print("Performing login for account " + username + "...")

        self.ui_control.click_on_position(constants.PROFILE_BUTTON)
        self.ui_control.click_on_position(constants.SIGNUP_BUTTON)
        self.ui_control.click_on_image_file(constants.BUTTON_ADD_ACCOUNT)
        self.ui_control.click_on_position(constants.USERNAME_BUTTON)
        self.ui_control.click_on_position(constants.EMAIL_BUTTON)

        self.ui_control.write(username)
        self.ui_control.press_enter()
        self.ui_control.write(password)

        self.ui_control.click_on_position(constants.LOGIN_BUTTON)
        time.sleep(constants.WAIT_FOR_CAPTCHA)

        # verify login
        home_button = self.ui_control.find_image(constants.BUTTON_HOME)

        if home_button is not None:
            print("Successfully logged in")
            return True

        return self.bypass_verification()

    def bypass_verification(self, attempts_number=constants.CAPTCHA_ATTEMPT_COUNT):

        print("Performing bypass captcha verification...")

        current_attempt = 0
        while current_attempt < attempts_number:
            print("Attempt: " + str(current_attempt + 1))

            for x in range(1, constants.PUZZLE_IMAGES_COUNT):
                puzzle_name = "res/puzzle" + str(x) + ".png"
                result = self.ui_control.find_image(puzzle_name, confidence=constants.CAPTCHA_CONFIDENCE)

                if result is not None and constants.CAPTCHA_MIN_X < result.left < constants.CAPTCHA_MAX_X\
                        and constants.CAPTCHA_MIN_Y < result.top < constants.CAPTCHA_MAX_Y:
                    self.ui_control.drag_and_drop(constants.INITIAL_MOUSE_POSITION_X, constants.INITIAL_MOUSE_POSITION_Y,
                                                  result.left, constants.INITIAL_MOUSE_POSITION_Y)
                    print("Successfully logged in")
                    return True

            self.ui_control.click_on_image_file(constants.BUTTON_CAPTCHA_REFRESH)
            current_attempt += 1

        return False

    def logout(self):

        print("Performing logout...")
        self.ui_control.click_on_position(constants.PROFILE_BUTTON)
        self.ui_control.click_on_position(constants.OPTION_BUTTON)
        self.ui_control.scroll_for_click(constants.BUTTON_LOGOUT, constants.DEFAULT_SCROLL_SIZE)
        self.ui_control.click_on_position(constants.LOGOUT_BUTTON)

    def debug_mouse_position(self):
        self.ui_control.debug_mouse_position()

    def follow_user_followers(self, username, delay, timeout):

        print("Performing following followers...")

        self.ui_control.click_on_position(constants.DISCOVER_BUTTON)
        self.ui_control.click_on_position(constants.SEARCH_BAR)
        self.ui_control.write(username)
        self.ui_control.click_on_position(constants.SEARCH_BUTTON)

        time.sleep(constants.WAIT_FOR_SEARCH_USER_RESULTS)
        self.ui_control.click_on_position(constants.FIRST_USER_IN_LIST)
        time.sleep(constants.CLICK_DELAY)
        self.ui_control.click_on_position(constants.FOLLOWERS_BUTTON)
        time.sleep(constants.WAIT_FOR_FOLLOWERS_RESULT)

        current_follow_count = 0
        initial_time = datetime.now()
        current_time = datetime.now()

        seconds_diff = current_time - initial_time

        while seconds_diff.seconds < timeout:
            success = self.ui_control.scroll_for_find(constants.BUTTON_FOLLOW, constants.DEFAULT_SCROLL_SIZE)
            if success:
                #Get userid
                userid_region = (success.left/constants.RESOLUTION_FACTOR - constants.REGION_X_OFFSET,
                                 success.top - constants.REGION_Y_OFFSET_USERID,
                                 constants.REGION_WIDTH, constants.REGION_HEIGHT)
                userid = self.ui_control.read_text_in_region(userid_region)
                print("username - " + userid)
                #get username
                username_region = (success.left/constants.RESOLUTION_FACTOR - constants.REGION_X_OFFSET,
                                   success.top + constants.REGION_Y_OFFSET_USERNAME,
                                   constants.REGION_WIDTH, constants.REGION_HEIGHT)
                username = self.ui_control.read_text_in_region(username_region)
                print("name - " + username)

                if(username is not "" and userid is not ""):
                    self.ui_control.click_on_image(success)
                    current_follow_count += 1
                    time.sleep(delay)
                else:
                    self.ui_control.scroll_screen_up(constants.DEFAULT_SCROLL_SIZE * 2)

            current_time = datetime.now()
            seconds_diff = current_time - initial_time

        self.back_to_home()
        return current_follow_count

    def watch_feed_videos(self, timeout):

        print("Performing watch videos on feed")

        current_watch_count = 0
        initial_time = datetime.now()
        current_time = datetime.now()

        seconds_diff = current_time - initial_time

        while seconds_diff.seconds < timeout:
            self.ui_control.scroll_screen_up(constants.DEFAULT_SCROLL_SIZE)
            time.sleep(random.randrange(constants.RANDOM_MIN_WAIT_WATCH_VIDEO, constants.RANDOM_MAX_WAIT_WATCH_VIDEO))
            current_watch_count += 1
            current_time = datetime.now()
            seconds_diff = current_time - initial_time

        self.back_to_home()
        return current_watch_count

    def like_by_hashtag(self, hashtag):

        print("Performing like by hashtag >>" + hashtag + "<< ...")

        self.ui_control.click_on_position(constants.DISCOVER_BUTTON)
        self.ui_control.click_on_position(constants.SEARCH_BAR)
        self.ui_control.write("#" + hashtag)
        self.ui_control.click_on_position(constants.SEARCH_BUTTON)

        time.sleep(constants.WAIT_FOR_HASHTAG_RESULTS)
        self.ui_control.click_on_position(constants.FIRST_HASHTAG_IN_LIST)
        self.ui_control.click_on_position(constants.FIRST_VIDEO_IN_HASHTAG_RESULT)
        #DO LIKE AND RETRIEVE USER
        self.ui_control.click_on_position(constants.TOP_BACK_BUTTON)
        self.ui_control.click_on_position(constants.SECOND_VIDEO_IN_HASHTAG_RESULT)
        # DO LIKE AND RETRIEVE USER
        self.ui_control.click_on_position(constants.TOP_BACK_BUTTON)
        self.ui_control.click_on_position(constants.THIRD_VIDEO_IN_HASHTAG_RESULT)
        self.ui_control.click_on_position(constants.TOP_BACK_BUTTON)

        self.ui_control.click_on_position(constants.TOP_BACK_BUTTON)
        self.ui_control.click_on_position(constants.TOP_BACK_BUTTON)
        self.ui_control.click_on_position(constants.HOME_BUTTON)

    def comment_on_feed(self, comments, delay, timeout):

        print("Performing comments on public feed")

        current_comment_count = 0
        initial_time = datetime.now()
        current_time = datetime.now()

        seconds_diff = current_time - initial_time

        while seconds_diff.seconds < timeout:
            self.ui_control.click_on_position(constants.COMMENT_BUTTON)
            self.ui_control.click_on_position(constants.COMMENT_BAR_ON_FEED)
            comments_size = len(comments)
            sorted_index = random.randrange(0, comments_size)
            self.ui_control.write(comments[sorted_index])
            self.ui_control.click_on_position(constants.SEND_COMMENT_BUTTON)
            current_comment_count += 1
            self.ui_control.click_on_position(constants.ANDROID_BACK_BUTTON)
            self.ui_control.scroll_screen_up(constants.DEFAULT_SCROLL_SIZE)

            current_time = datetime.now()
            seconds_diff = current_time - initial_time
            time.sleep(delay)

        self.back_to_home()
        return current_comment_count

    def random_scroll_up(self):

        random_number = random.randrange(2, 7)
        for x in range(1, random_number):
            self.ui_control.scroll_screen_up(constants.DEFAULT_SCROLL_SIZE)


    def like_followers_of(self, username, delay, timeout):

        print("Performing liking followers...")

        self.ui_control.click_on_position(constants.DISCOVER_BUTTON)
        self.ui_control.click_on_position(constants.SEARCH_BAR)
        self.ui_control.write(username)
        self.ui_control.click_on_position(constants.SEARCH_BUTTON)

        time.sleep(constants.WAIT_FOR_SEARCH_USER_RESULTS)
        self.ui_control.click_on_position(constants.FIRST_USER_IN_LIST)
        time.sleep(constants.CLICK_DELAY)
        self.ui_control.click_on_position(constants.FOLLOWERS_BUTTON)
        time.sleep(constants.WAIT_FOR_FOLLOWERS_RESULT)

        current_like_amount = 0
        initial_time = datetime.now()
        current_time = datetime.now()

        seconds_diff = current_time - initial_time

        while seconds_diff.seconds < timeout:
            self.random_scroll_up()
            self.ui_control.click_on_position(constants.FIRST_USER_IN_FOLLOWERS_LIST)

            has_post = self.ui_control.find_image(constants.ICON_MINI_PLAY)
            if has_post:
                self.ui_control.click_on_position(constants.FIRST_POST_ON_USER_FEED)
                self.ui_control.click_on_position(constants.LIKE_BUTTON)
                current_like_amount += 1
                self.ui_control.click_on_position(constants.TOP_BACK_BUTTON)
                self.ui_control.click_on_position(constants.TOP_BACK_BUTTON)
            else:
                self.ui_control.click_on_position(constants.TOP_BACK_BUTTON)

            current_time = datetime.now()
            seconds_diff = current_time - initial_time

            time.sleep(delay)

        self.back_to_home()
        return current_like_amount


    def back_to_home(self):

        home_button = self.ui_control.find_image(constants.BUTTON_HOME)
        while home_button is None:
            self.ui_control.click_on_position(constants.ANDROID_BACK_BUTTON)
            home_button = self.ui_control.find_image(constants.BUTTON_HOME)




