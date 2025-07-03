# 🛡️ Keylogger with Screenshot Capture – GUI Version

This project is a Python-based GUI application that captures both **keystrokes** and **screenshots** at regular intervals. Designed to be user-friendly and fully functional, this tool was built as part of my internship at **Cantilever**.


## 🎯 Features

- ✅ **Graphical User Interface** built using `tkinter`
- 🖥️ Captures screenshots every X seconds (user-defined)
- ⌨️ Logs all keystrokes to a timestamped file
- 📂 Lets user select output folder to store logs
- 🧵 Uses multithreading for non-blocking performance
- 🛑 Press `ESC` anytime to stop logging
- 📁 Organized output folder with both screenshots and logs


## 📸 GUI Preview

![image](https://github.com/user-attachments/assets/b77f3bd1-36f2-44c0-9be8-831f902b91e7)


## 🚀 Getting Started

### 🔧 Requirements

Make sure you have Python installed. Then install dependencies:

```bash
pip install pynput pyautogui
