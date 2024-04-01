from time import sleep

from pyautogui import screenshot
from os.path import exists


def take_screenshot(path) -> bool:
    screenshot().save(path)
    return exists(path)

if __name__ == '__main__':
    sleep(3)
    take_screenshot('./shots/shot1.png')
