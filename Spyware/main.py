from Logger.tracker import keyboard_listener, save_time

if __name__ == '__main__':
    save_time('Logger/LOG.txt', 'Started at ')  # Saves the start time in LOG.txt
    keyboard_listener()  # Tracks the use keyboard inputs and saves them in LOG.txt
    save_time('Logger/LOG.txt', 'Ended at ', extra_endline=True)  # Saves the end time in LOG.txt
