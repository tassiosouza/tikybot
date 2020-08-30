import pyautogui
import time
import pytesseract
import constants
import random
from datetime import datetime

class UiControl:

    def __init__(self, x=0):
        self.x = x
        self.pyautogui = pyautogui

    @staticmethod
    def focus(INITIAL_MOUSE_POSITION_X, INITIAL_MOUSE_POSITION_Y):
        pyautogui.click(INITIAL_MOUSE_POSITION_X, INITIAL_MOUSE_POSITION_Y)
        time.sleep(constants.CLICK_IMAGE_DELAY)

    def click_on_image_file(self, image_name):
        button = pyautogui.locateOnScreen(image_name, confidence=0.8)
        if button is not None:
            self.click_on_image(button)
            return button
        else:
            print("Could not find button image - " + image_name)
            return None


    def click_on_image(self, image, delay=constants.CLICK_IMAGE_DELAY):
        if image is not None:
            if constants.IS_RETINA_DISPLAY:
                x = image.left / constants.RETINA_POS_FACTOR + image.width / constants.RETINA_SIZE_FACTOR
                y = image.top / constants.RETINA_POS_FACTOR + image.height / constants.RETINA_SIZE_FACTOR
                self.click_on_position((x, y))
            else:
                pyautogui.click(image)
            time.sleep(delay if delay != 0 else 1)
            return image
        else:
            return None

    @staticmethod
    def click_on_position(position):
        pos_x, pos_y = position
        pyautogui.click(pos_x, pos_y)
        time.sleep(constants.CLICK_DELAY)

    @staticmethod
    def drag_and_drop(initial_x, initial_y, final_x, final_y):
        pyautogui.moveTo(initial_x, initial_y)
        pyautogui.dragTo(final_x, final_y, constants.MOUSE_MOVE_SPEED, button='left')
        time.sleep(constants.CLICK_IMAGE_DELAY)

    @staticmethod
    def write(value):
        pyautogui.typewrite(value)
        time.sleep(constants.CLICK_IMAGE_DELAY)

    @staticmethod
    def press_enter():
        pyautogui.press('enter')
        time.sleep(constants.CLICK_IMAGE_DELAY)

    @staticmethod
    def find_image(image_name, confidence=constants.DEFAULT_CONFIDENCE):
        result = pyautogui.locateOnScreen(image_name, confidence=confidence)
        time.sleep(constants.CLICK_IMAGE_DELAY)
        if result is not None:
            return result
        else:
            print("Could not find image - " + image_name)
            return None

    def scroll_for_click(self, image_name):
        image_result = pyautogui.locateOnScreen(image_name, confidence=constants.DEFAULT_CONFIDENCE)
        while image_result is None:
            self.scroll_screen_up()
            time.sleep(constants.CLICK_IMAGE_DELAY)
            print("Scrolling for find - " + image_name)
            image_result = pyautogui.locateOnScreen(image_name, confidence=constants.DEFAULT_CONFIDENCE)

        self.click_on_image(image_result)
        time.sleep(constants.CLICK_IMAGE_DELAY)
        return image_result

    def scroll_for_find(self, image_name, delay=constants.CLICK_IMAGE_DELAY, confidence=constants.DEFAULT_CONFIDENCE, grayscale=False):

        initial_time = datetime.now()
        current_time = datetime.now()

        seconds_diff = current_time - initial_time
        screen_coordinates = (constants.SCREEN_X0,constants.SCREEN_X1, constants.SCREEN_Y0, constants.SCREEN_Y1)
        image_result = pyautogui.locateOnScreen(image_name, confidence=confidence, grayscale=grayscale, region=(10,17, 392, 999))
        while image_result is None and seconds_diff.seconds < 10:
            time.sleep(constants.CLICK_IMAGE_DELAY)
            print("Scrolling for find - " + image_name)
            self.scroll_screen_up()
            image_result = pyautogui.locateOnScreen(image_name, confidence=confidence, grayscale=grayscale, region=(10, 17, 392, 999))

            current_time = datetime.now()
            seconds_diff = current_time - initial_time

        time.sleep(delay)
        return image_result

    @staticmethod
    def scroll_screen_up():
        pyautogui.moveTo(constants.INITIAL_MOUSE_POSITION_X, constants.INITIAL_MOUSE_POSITION_Y)
        pyautogui.dragTo(constants.INITIAL_MOUSE_POSITION_X, constants.INITIAL_MOUSE_POSITION_Y - 450, 0.8, button='left')
        time.sleep(constants.CLICK_IMAGE_DELAY)

    @staticmethod
    def debug_mouse_position():
        while True:
            pos_x, pos_y = pyautogui.position()
            print("PosX - " + str(pos_x) + " | PosY - " + str(pos_y))
            time.sleep(constants.DEBUG_MOUSE_UPDATE_DELAY)

    @staticmethod
    def read_text_in_region(region):
        image = pyautogui.screenshot(region=region)
        return pytesseract.image_to_string(image)

    @staticmethod
    def print_screen(region):
        image = pyautogui.screenshot(region=region)
        return image



