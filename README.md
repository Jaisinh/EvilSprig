# EvilSprig

**EvilSprig** is a mischievous project that transforms a normal Sprig into an *evil* device by leveraging the power of CircuitPython and the HID library. With this, you can automate keystrokes to execute pranks, like directing unsuspecting users to the infamous Rick Roll!

---

## Features

- **Turns your Sprig evil**: Automatically types and executes commands or URLs.
- **Built using CircuitPython**: Utilizes the HID library to simulate a keyboard.
- **Compact and efficient**: Minimal code to achieve maximum impact.
- **Rick Roll prank included**: Redirects to everyone's favorite URL.

---

## How It Works

EvilSprig acts as a USB HID device that mimics a keyboard. Upon connection, it performs the following steps:
1. Waits for a few seconds to ensure the system is ready.
2. Simulates opening the browser (via `COMMAND + SPACE`, then typing "Safari").
3. Automatically types a Rick Roll URL (`bit.ly/3P4lQBj`) and presses Enter.
4. Enjoy the chaos!

---

## Setup Instructions

### Requirements
- A **Sprig** console with CircuitPython support.
- CircuitPython libraries:
  - `adafruit_hid`
  
### Installation
1. Clone this repository or download the ZIP.
2. Copy the `code.py` file to your Sprig's filesystem.
3. Ensure the required libraries are in the `lib/` folder of your device.
   - Specifically, include the `adafruit_hid` library.
4. Connect your Sprig to a computer via USB.

### Usage
1. Plug in the EvilSprig to a computer.
2. The device waits for 5 seconds to allow the system to stabilize.
3. It opens the browser and types the Rick Roll URL.
4. Watch your unsuspecting target enjoy the fun! 🎵

---

## Code Overview

The core functionality is implemented using the following:
- **CircuitPython HID Library**: Simulates keyboard keypresses.
- **Predefined Commands**: Sends specific keystrokes to open a browser and navigate to a URL.

### Key Functions
- `type_text(text)`: Types a given string character by character, handling special keys (e.g., numbers, periods, etc.).
- `keyboard.press()`: Simulates a keypress.
- `keyboard.release_all()`: Releases all pressed keys.

---

## Disclaimer

This project is purely for educational and entertainment purposes. Please ensure you have permission before using EvilSprig on someone else's computer. Misuse of this project may result in unintended consequences.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute, but please give credit where it's due!

---

## Contributing

Contributions are welcome! If you have ideas for improving EvilSprig or adding more features, feel free to submit a pull request.

---

## Acknowledgments

- Inspired by the Hack Club's Sprig console.
- Special thanks to the CircuitPython community for their amazing libraries.
- Dedicated to spreading a little chaos with a good laugh!

---

**Stay Evil. Stay Mischievous.**
