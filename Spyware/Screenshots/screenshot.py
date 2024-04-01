from pyautogui import screenshot
from os.path import exists


def take_screenshot(path) -> bool:
    screenshot().save(path)
    return exists(path)


