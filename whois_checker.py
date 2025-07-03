import tkinter as tk
from tkinter import messagebox, filedialog
import whois
import csv
import os
from datetime import datetime

def fetch_domain_info(domain):
    try:
        w = whois.whois(domain)

        if not w.domain_name:
            raise ValueError("No WHOIS info found.")

        creation = w.creation_date[0] if isinstance(w.creation_date, list) else w.creation_date
        expiration = w.expiration_date[0] if isinstance(w.expiration_date, list) else w.expiration_date
        name_servers = ', '.join(w.name_servers) if isinstance(w.name_servers, list) else w.name_servers

        return {
            "Domain": domain,
            "Registrar": w.registrar or "N/A",
            "Creation Date": creation or "N/A",
            "Expiration Date": expiration or "N/A",
            "Name Servers": name_servers or "N/A",
            "Checked At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch info for {domain}.\n\n{e}")
        return None

def save_to_csv(data, filename="output/domain_info.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    file_exists = os.path.isfile(filename)

    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

def check_domain():
    domain = domain_entry.get().strip()
    if not domain:
        messagebox.showwarning("Missing Input", "Please enter a domain name.")
        return

    result = fetch_domain_info(domain)
    if result:
        output = (
            f"Registrar: {result['Registrar']}\n"
            f"Creation Date: {result['Creation Date']}\n"
            f"Expiration Date: {result['Expiration Date']}\n"
            f"Name Servers: {result['Name Servers']}\n"
        )
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, output)

        save_to_csv(result)
        status_label.config(text="✅ Result saved to output/domain_info.csv", fg="green")

# === GUI Setup ===
window = tk.Tk()
window.title("Domain WHOIS Lookup Tool")
window.geometry("500x400")
window.resizable(False, False)

tk.Label(window, text="Enter Domain (e.g., google.com):").pack(pady=10)
domain_entry = tk.Entry(window, width=40)
domain_entry.pack()

tk.Button(window, text="Check WHOIS", command=check_domain, bg="#4CAF50", fg="white").pack(pady=10)

result_text = tk.Text(window, height=10, width=60)
result_text.pack(pady=10)

status_label = tk.Label(window, text="Status: Idle", fg="gray")
status_label.pack(pady=5)

window.mainloop()
