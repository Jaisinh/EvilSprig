import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

def type_text(text):
    for char in text:
        if char.isupper():  
            keyboard.press(Keycode.SHIFT, getattr(Keycode, char.upper()))
            keyboard.release_all()
        elif char == ".":  # Special case for "."
            keyboard.press(Keycode.PERIOD)
            keyboard.release_all()
        elif char == "/":  # Special case for "/"
            keyboard.press(Keycode.FORWARD_SLASH)
            keyboard.release_all()
        elif char == ":":  # Special case for ":"
            keyboard.press(Keycode.SHIFT, Keycode.SEMICOLON)
            keyboard.release_all()
        elif char == "-":  # Special case for "-"
            keyboard.press(Keycode.MINUS)
            keyboard.release_all()
        elif char == "3":  # Special case for "3"
            keyboard.press(Keycode.THREE)
            keyboard.release_all()
        elif char == "4":  # Special case for "4"
            keyboard.press(Keycode.FOUR)
            keyboard.release_all()
        else:
            try:
                keyboard.press(getattr(Keycode, char.upper()))  # Press other keys
                keyboard.release_all()
            except AttributeError:
                print(f"Unsupported character: {char}")

fake_update_url = "www.whitescreen.online/fake-mac-os-x-update-screen"

keyboard.press(Keycode.COMMAND, Keycode.SPACE)
keyboard.release_all()
time.sleep(0.3)

type_text("Brave")
time.sleep(0.3)

keyboard.press(Keycode.ENTER)
keyboard.release_all()
time.sleep(1.5)  

type_text(fake_update_url)
keyboard.press(Keycode.ENTER)
keyboard.release_all()
time.sleep(3)  

keyboard.press(Keycode.F)
keyboard.release_all()

