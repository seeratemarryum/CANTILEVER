# 🛡️ Internship Projects – Cantilever

Welcome to my internship project repository for **Cantilever**. This repository documents my learning journey and contributions during the internship program. Each project is hosted on a dedicated branch and showcases real-world skills in cybersecurity, Python automation, and digital forensics.


## 🚀 Projects Overview

### 🔐 [Keylogger with Screenshot Capture](https://github.com/seeratemarryum/CANTILEVER/tree/KeyLogger)
A multi-threaded Python script that captures keystrokes and periodic screenshots from the user’s machine. Useful for security monitoring or understanding how malware behaves.

- 📌 Technologies: `pynput`, `pyautogui`, `threading`, `logging`
- ✅ Press ESC to stop the logger
- 📝 Output includes timestamped folders with screenshots and key logs
- 📂 Logs are saved locally in structured folders


### 🌐 [WHOIS Domain Info Checker](https://github.com/seeratemarryum/CANTILEVER/tree/Domain-Lookup)
A tool to query WHOIS data for any domain, extracting registrar, creation/expiration dates, and name server info. Outputs results to a CSV for further analysis.

- 📌 Technologies: `python-whois`, `csv`, `datetime`, `os`
- 🧠 Handles protected or invalid domain responses gracefully
- 📁 Saves results to `output/domain_info.csv`


## 🧰 Technologies Used

- Python 3.x
- VS Code
- Git & GitHub
- `pynput`, `pyautogui`, `python-whois`, `csv`, `datetime`, `threading`


## 📂 Repository Structure

```bash
├── main (this branch: overview of internship)
├── keylogger         # Project 1
├── domain-checker    # Project 2
