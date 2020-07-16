import pyautogui
import time
import pytesseract
import constants

class UiControl:

    def __init__(self, x=0):
        self.x = x
        self.pyautogui = pyautogui

    @staticmethod
    def focus(INITIAL_MOUSE_POSITION_X, INITIAL_MOUSE_POSITION_Y):
        pyautogui.click(INITIAL_MOUSE_POSITION_X, INITIAL_MOUSE_POSITION_Y)
        time.sleep(constants.CLICK_IMAGE_DELAY)

    @staticmethod
    def click_on_image_file(image_name):
        button = pyautogui.locateOnScreen(image_name, confidence=0.8)
        time.sleep(constants.CLICK_IMAGE_DELAY)
        if button is not None:
            pyautogui.click(button)
            time.sleep(constants.CLICK_IMAGE_DELAY)
        else:
            print("Could not find button image - " + image_name)

    @staticmethod
    def click_on_image(image):
        time.sleep(constants.CLICK_IMAGE_DELAY)
        if image is not None:
            pyautogui.click(image)
            time.sleep(constants.CLICK_IMAGE_DELAY)
        else:
            print("Could not find button image - " + image)

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

    @staticmethod
    def scroll_for_click(image_name, scroll_size):
        image_result = pyautogui.locateOnScreen(image_name, confidence=constants.DEFAULT_CONFIDENCE)
        while image_result is None:
            pyautogui.scroll(-scroll_size, x=constants.INITIAL_MOUSE_POSITION_X, y=constants.INITIAL_MOUSE_POSITION_Y)
            time.sleep(constants.CLICK_IMAGE_DELAY)
            print("Scrolling for find - " + image_name)
            image_result = pyautogui.locateOnScreen(image_name, confidence=constants.DEFAULT_CONFIDENCE)

        pyautogui.click(image_result)
        time.sleep(constants.CLICK_IMAGE_DELAY)
        return image_result

    @staticmethod
    def scroll_for_find(image_name, scroll_size):
        image_result = pyautogui.locateOnScreen(image_name, confidence=constants.DEFAULT_CONFIDENCE)
        while image_result is None:
            pyautogui.scroll(-scroll_size, x=constants.INITIAL_MOUSE_POSITION_X, y=constants.INITIAL_MOUSE_POSITION_Y)
            time.sleep(constants.CLICK_IMAGE_DELAY)
            print("Scrolling for find - " + image_name)
            image_result = pyautogui.locateOnScreen(image_name, confidence=constants.DEFAULT_CONFIDENCE)

        time.sleep(constants.CLICK_IMAGE_DELAY)
        return image_result

    @staticmethod
    def scroll_screen_up(scroll_size):
        pyautogui.scroll(-scroll_size, x=constants.INITIAL_MOUSE_POSITION_X, y=constants.INITIAL_MOUSE_POSITION_Y)
        time.sleep(constants.CLICK_IMAGE_DELAY)

    @staticmethod
    def debug_mouse_position():
        while True:
            pos_x, pos_y = pyautogui.position()
            print("PosX - " + str(pos_x) + " | PosY - " + str(pos_y))
            time.sleep(constants.CLICK_IMAGE_DELAY)

    @staticmethod
    def read_text_in_region(region):
        image = pyautogui.screenshot(region=region)
        return pytesseract.image_to_string(image)





