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
        elif char == ".":
            keyboard.press(Keycode.PERIOD) 
            keyboard.release_all()
        elif char == "/":
            keyboard.press(Keycode.FORWARD_SLASH)  
            keyboard.release_all()
        elif char == ":":
            keyboard.press(Keycode.SHIFT, Keycode.SEMICOLON)  
            keyboard.release_all()
        elif char == "3":
            keyboard.press(Keycode.THREE)  
            keyboard.release_all()
        elif char == "4":
            keyboard.press(Keycode.FOUR)  
            keyboard.release_all()
        else:
            try:
                keyboard.press(getattr(Keycode, char.upper()))  
                keyboard.release_all()
            except AttributeError:
                print(f"Unsupported character: {char}")


rick_roll_url = "bit.ly/3P4lQBj"


keyboard.press(Keycode.COMMAND, Keycode.SPACE)  
keyboard.release_all()
time.sleep(0.3)

type_text("Brave")  
time.sleep(0.3)

keyboard.press(Keycode.ENTER)  
keyboard.release_all()
time.sleep(0.3)

type_text(rick_roll_url) 
keyboard.press(Keycode.ENTER)  
keyboard.release_all()
