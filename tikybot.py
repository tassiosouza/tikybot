import pyautogui
import time
import random

#Those values depends on screen resolution and emulator position

#Captcha verification
CAPTCHA_MIN_X = 160
CAPTCHA_MAX_X = 338
CAPTCHA_MIN_Y = 360
CAPTCHA_MAX_Y = 505
INITIAL_MOUSE_POSITION_X = 109
INITIAL_MOUSE_POSITION_Y = 432
MOUSE_MOVE_SPEED = 2

#Buttons
BUTTON_PROFILE = "res/profile_button.png"
BUTTON_SIGNUP = "res/signup_button.png"
BUTTON_ADD_ACCOUNT = "res/add_account_button.png"
BUTTON_USERNAME = "res/username_button.png"
BUTTON_EMAIL = "res/email_button.png"
BUTTON_LARGE_LOGIN = "res/large_login_button.png"
BUTTON_CAPTCHA_REFRESH = "res/refresh_captcha.png"

class Tikybot():

    def __init__(self, x=0):
        self.x = x
        pyautogui.click(CAPTCHA_MAX_X,CAPTCHA_MAX_Y)

    def login(self, username, password):
        profile_button = pyautogui.locateOnScreen(BUTTON_PROFILE, confidence=0.8)
        time.sleep(1)
        pyautogui.click(profile_button)
        time.sleep(1)
        signup_button = pyautogui.locateOnScreen(BUTTON_SIGNUP, confidence=0.8)
        time.sleep(1)
        pyautogui.click(signup_button)
        time.sleep(1)
        add_account_button = pyautogui.locateOnScreen(BUTTON_ADD_ACCOUNT, confidence=0.8)
        time.sleep(1)
        pyautogui.click(add_account_button)
        time.sleep(1)
        username_button = pyautogui.locateOnScreen(BUTTON_USERNAME, confidence=0.8)
        time.sleep(1)
        pyautogui.click(username_button)
        time.sleep(1)
        email_button = pyautogui.locateOnScreen(BUTTON_EMAIL, confidence=0.8)
        time.sleep(1)
        pyautogui.click(email_button)
        time.sleep(1)
        pyautogui.typewrite(username)
        pyautogui.press('enter')
        pyautogui.typewrite(password)
        time.sleep(1)
        large_login_button = pyautogui.locateOnScreen(BUTTON_LARGE_LOGIN, confidence=0.8)
        time.sleep(1)
        pyautogui.click(large_login_button)
        time.sleep(3)
        return self.bypass_verification()

    def bypass_verification(self, attempts_number=3):
        print("Trying to bypass captcha verification...")
        current_attempt = 0
        while current_attempt < attempts_number:
            print("Attempt: " + str(current_attempt + 1))

            for x in range(1, 11):
                puzzle_name = "res/puzzle" + str(x) + ".png"
                result = pyautogui.locateOnScreen(puzzle_name, confidence=0.6)

                if result is not None and CAPTCHA_MIN_X < result.left < CAPTCHA_MAX_X\
                        and CAPTCHA_MIN_Y < result.top < CAPTCHA_MAX_Y:
                    pyautogui.moveTo(INITIAL_MOUSE_POSITION_X, INITIAL_MOUSE_POSITION_Y)
                    pyautogui.dragTo(result.left, INITIAL_MOUSE_POSITION_Y, MOUSE_MOVE_SPEED, button='left')
                    return True
            time.sleep(1)
            captcha_refresh_button = pyautogui.locateOnScreen(BUTTON_CAPTCHA_REFRESH, confidence=0.8)
            time.sleep(1)
            pyautogui.click(captcha_refresh_button)
            current_attempt += 1
        return False