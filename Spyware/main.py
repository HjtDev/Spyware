from Logger.tracker import keyboard_listener, save_time

if __name__ == '__main__':
    save_time('Logger/LOG.txt', 'Started at ')
    keyboard_listener()
    save_time('Logger/LOG.txt', 'Ended at ', extra_endline=True)
