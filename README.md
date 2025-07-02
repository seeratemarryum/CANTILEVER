# 🌐 WHOIS Domain Info Checker

A simple Python script to fetch and save WHOIS information for any domain. The tool uses the `whois` library to extract registrar details, creation and expiration dates, and DNS name servers, then logs the results into a CSV file for later reference.

---

## 🚀 Features

- 🧠 Fetches domain info using Python’s `whois` library
- 📅 Displays:
  - Domain registrar
  - Creation date
  - Expiration date
  - Name servers
- 📂 Saves output in `output/domain_info.csv`
- ⚠️ Handles:
  - Protected/invalid domains
  - Missing or null WHOIS fields

---

## 🛠️ Requirements

Install the required library using pip:

```bash
pip install python-whois
