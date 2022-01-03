import ctypes, time
import threading
import sys
from pynput import keyboard

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

class myKey():
    Q = 0x10
    W = 0x11
    E = 0x12
    R = 0x13
    T = 0x14
    Y = 0x15
    U = 0x16
    I = 0x17
    O = 0x18
    P = 0x19
    
    A = 0x1E
    S = 0x1F
    D = 0x20
    F = 0x21
    G = 0x22
    H = 0x23
    J = 0x24
    K = 0x25
    L = 0x26

    Z = 0x2C
    X = 0x2D
    C = 0x2E
    V = 0x2F
    B = 0x30
    N = 0x31
    M = 0x32

    LSHIFT = 0x2A
    SPACE = 0x39

    LARROW = 0xCB
    UARROW = 0xC8
    RARROW = 0xCD
    DARROW = 0xD0


# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def press(hexKeyCode,interval=.05):
    PressKey(hexKeyCode)
    time.sleep(interval)
    ReleaseKey(hexKeyCode)

# Change this part
def main_loop():
    counter = 0
    press(myKey.UARROW)
    press(myKey.UARROW)
    time.sleep(0.1)
    press(myKey.T)
    press(myKey.T)
    press(myKey.T)
    time.sleep(0.1)
    press(myKey.UARROW)
    press(myKey.UARROW)
    time.sleep(0.1)
    press(myKey.LSHIFT)
    press(myKey.LSHIFT)
    press(myKey.LSHIFT)
    time.sleep(0.1)
    press(myKey.DARROW)
    press(myKey.DARROW)
    time.sleep(0.1)
    press(myKey.T)
    press(myKey.T)
    press(myKey.T)
    time.sleep(0.1)
    press(myKey.DARROW)
    press(myKey.DARROW)
    time.sleep(0.1)
    press(myKey.LSHIFT)
    press(myKey.LSHIFT)
    press(myKey.LSHIFT)
    time.sleep(0.1)
    press(myKey.F)
    press(myKey.F)
    press(myKey.F)
    time.sleep(0.1)


stop_send_key = 0 
kill_all_thread = 0

def send_key_thread():
    global stop_send_key
    while True:
        if stop_send_key == 0:
            main_loop();
        if kill_all_thread == 1:
            break


def on_press(key):
    global stop_send_key
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))

    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        if key == keyboard.Key.alt:
            if(stop_send_key == 0):
                print("You pressed . stop sending keystrokes")
                stop_send_key = 1
            else:
                print("You pressed . resume sending keystrokes")
                stop_send_key = 0

def on_activate_c():
    print('Ctrl+C activated!')
    kill_all_thread = 1

def for_canonical(f):
    return lambda k: f(t3.canonical(k))

if __name__ == "__main__":
    try:
        t2 = threading.Thread(target=send_key_thread)
        t2.daemon = True

        # #t1.start()
        t2.start()

        # # with keyboard.GlobalHotKeys({
        # # '<ctrl>+c': on_activate_c}) as h:
        # #     h.join()
        while t2.is_alive():
            t2.join(1)
    except KeyboardInterrupt:
        print('You pressed ctrl+c')
        kill_all_thread = 1
        t2.join()









