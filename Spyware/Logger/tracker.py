from pynput.keyboard import Listener
from datetime import datetime as dt


def convert_key(key) -> str:
    """
    Gets a key with the format of pynput and converts it to a raw key
    :param key: pynput format key
    :return: raw key as a string
    """
    return str(key).replace("'", '').split('.')[-1]


def save_time(file: str, name, extra_endline=False) -> None:
    """
    Saves current time into given file.
    :param file: The path to the logging file from the executed script.
    :param name: It Will be the title of the saved time, so you can check what this time is for.
    :param extra_endline: Adding an extra end line can help with cleaner output when we have multiple logging time in one file
    :return: None
    """
    with open(file, 'a') as f:
        f.write(name + str(dt.now()) + '\n' * (2 if extra_endline else 1))


def on_press(key) -> None:
    """
    This function will get a key as input from pynput tracker and writes to LOG.txt with couple of changes for better output result
    :param key: pynput format key
    :return: None
    """
    key = convert_key(key)
    with open('Logger/LOG.txt', 'a') as file:
        if len(key) == 1:
            file.write(key)
        elif len(key) > 1 and key != 'space':
            file.write('\n' + key + '\n')
        else:
            file.write('\n')


def on_release(key) -> bool | None:
    """
    It is the function that specifies when tracking should end in this case 'right shift press'
    :param key: pynput format key
    :return: None
    """
    key = convert_key(key)
    return False if key == 'shift_r' else None


def keyboard_listener() -> None:
    """
    Main keyboard listener that tracks your keyboard inputs
    :return: None
    """
    with Listener(on_press=on_press, on_release=on_release) as keyboard:
        keyboard.join()


if __name__ == '__main__':
    print(convert_key('Key.ctrl_l'))
    print(convert_key('Key.shift_r'))
    print(convert_key('Key.a'))
    print(convert_key('Key.esc'))
