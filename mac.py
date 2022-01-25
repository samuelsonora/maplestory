# Actuals Functions

import time
from pynput.keyboard import Key,Listener

kill_all_thread = 0

# def on_press(key):
#     global stop_send_key
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))

#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))
#         if key == keyboard.Key.alt:
#             if(stop_send_key == 0):
#                 print("You pressed . stop sending keystrokes")
#                 stop_send_key = 1
#             else:
#                 print("You pressed . resume sending keystrokes")
#                 stop_send_key = 0

# def on_activate_c():
#     print('Ctrl+C activated!')
#     kill_all_thread =1 

def foo():
    while True:
        print("test")
        time.sleep(2)
        if(kill_all_thread == 1):
            break
def boo():
    while True:

        keyboard.wait('q')
        print("q was pressed")
        if(kill_all_thread == 1):
            break

def on_release(key):
    print("{} key is released".format(key))
    if key == Key.q:
        return False

if __name__ == "__main__":
    try:
        t1 = threading.Thread(target=foo)
        t1.start()

        with Listener(on_release=on_release) as listener:
            listener.join()
        
        t1.join()
    except KeyboardInterrupt:
        print('You pressed ctrl+c')
        kill_all_thread = 1
