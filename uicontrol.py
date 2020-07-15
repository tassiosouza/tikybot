import pyautogui
import time
import pytesseract

INITIAL_MOUSE_POSITION_X = 109
INITIAL_MOUSE_POSITION_Y = 432
CLICK_IMAGE_DELAY = 1
CLICK_DELAY = 1
MOUSE_MOVE_SPEED = 1


class UiControl:

    def __init__(self, x=0):
        self.x = x
        self.pyautogui = pyautogui

    @staticmethod
    def focus():
        pyautogui.click(INITIAL_MOUSE_POSITION_X, INITIAL_MOUSE_POSITION_Y)
        time.sleep(CLICK_IMAGE_DELAY)

    @staticmethod
    def click_on_image_file(image_name):
        button = pyautogui.locateOnScreen(image_name, confidence=0.8)
        time.sleep(CLICK_IMAGE_DELAY)
        if button is not None:
            pyautogui.click(button)
            time.sleep(CLICK_IMAGE_DELAY)
        else:
            print("Could not find button image - " + image_name)

    @staticmethod
    def click_on_image(image):
        time.sleep(CLICK_IMAGE_DELAY)
        if image is not None:
            pyautogui.click(image)
            time.sleep(CLICK_IMAGE_DELAY)
        else:
            print("Could not find button image - " + image_name)

    @staticmethod
    def click_on_position(position):
        pos_x, pos_y = position
        pyautogui.click(pos_x, pos_y)
        time.sleep(CLICK_DELAY)

    @staticmethod
    def drag_and_drop(initial_x, initial_y, final_x, final_y):
        pyautogui.moveTo(initial_x, initial_y)
        pyautogui.dragTo(final_x, final_y, MOUSE_MOVE_SPEED, button='left')
        time.sleep(CLICK_IMAGE_DELAY)

    @staticmethod
    def write(value):
        pyautogui.typewrite(value)
        time.sleep(CLICK_IMAGE_DELAY)

    @staticmethod
    def press_enter():
        pyautogui.press('enter')
        time.sleep(CLICK_IMAGE_DELAY)

    @staticmethod
    def find_image(image_name, confidence=0.8):
        result = pyautogui.locateOnScreen(image_name, confidence=confidence)
        time.sleep(CLICK_IMAGE_DELAY)
        if result is not None:
            return result
        else:
            print("Could not find image - " + image_name)
            return None

    @staticmethod
    def scroll_for_click(image_name):
        image_result = pyautogui.locateOnScreen(image_name, confidence=0.8)
        while image_result is None:
            pyautogui.scroll(-10, x=INITIAL_MOUSE_POSITION_X, y=INITIAL_MOUSE_POSITION_Y)
            time.sleep(CLICK_IMAGE_DELAY)
            print("Scrolling for find - " + image_name)
            image_result = pyautogui.locateOnScreen(image_name, confidence=0.8)

        pyautogui.click(image_result)
        time.sleep(CLICK_IMAGE_DELAY)
        return image_result

    @staticmethod
    def scroll_for_find(image_name):
        image_result = pyautogui.locateOnScreen(image_name, confidence=0.8)
        while image_result is None:
            pyautogui.scroll(-10, x=INITIAL_MOUSE_POSITION_X, y=INITIAL_MOUSE_POSITION_Y)
            time.sleep(CLICK_IMAGE_DELAY)
            print("Scrolling for find - " + image_name)
            image_result = pyautogui.locateOnScreen(image_name, confidence=0.8)

        time.sleep(CLICK_IMAGE_DELAY)
        return image_result

    @staticmethod
    def scroll_screen_up(scroll_size):
        pyautogui.scroll(-scroll_size, x=INITIAL_MOUSE_POSITION_X, y=INITIAL_MOUSE_POSITION_Y)
        time.sleep(CLICK_IMAGE_DELAY)

    @staticmethod
    def debug_mouse_position():
        while True:
            pos_x, pos_y = pyautogui.position()
            print("PosX - " + str(pos_x) + " | PosY - " + str(pos_y))
            time.sleep(CLICK_IMAGE_DELAY)

    @staticmethod
    def read_text_in_region(region):
        image = pyautogui.screenshot(region=region)
        return pytesseract.image_to_string(image)





