from pynput.keyboard import Listener


def convert_key(key) -> str:
    return str(key).replace("'", '').split('.')[-1]


def keyboard_listener() -> None:
    with Listener(on_press=None, on_release=None) as keyboard:
        keyboard.join()


if __name__ == '__main__':
    print(convert_key('Key.ctrl_l'))
    print(convert_key('Key.shift_r'))
    print(convert_key('Key.a'))
    print(convert_key('Key.esc'))
