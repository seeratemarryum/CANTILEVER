import whois
import csv
import os
from datetime import datetime

def fetch_domain_info(domain):
    try:
        w = whois.whois(domain)

        if not w.domain_name:
            raise ValueError("No WHOIS info found. Domain may be protected or invalid.")

        # Handle datetime lists by selecting the first element
        creation = w.creation_date[0] if isinstance(w.creation_date, list) else w.creation_date
        expiration = w.expiration_date[0] if isinstance(w.expiration_date, list) else w.expiration_date
        name_servers = ', '.join(w.name_servers) if isinstance(w.name_servers, list) else w.name_servers

        print("\n--- Domain Information ---")
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {creation}")
        print(f"Expiration Date: {expiration}")
        print(f"Name Servers: {name_servers}")

        return {
            "Domain": domain,
            "Registrar": w.registrar or "N/A",
            "Creation Date": creation or "N/A",
            "Expiration Date": expiration or "N/A",
            "Name Servers": name_servers or "N/A",
            "Checked At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    except Exception as e:
        print(f"\n[!] Error fetching WHOIS data: {e}")
        return None

def save_to_csv(data, filename="output/domain_info.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    file_exists = os.path.isfile(filename)

    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)

    print(f"\n✅ Results saved to {filename}")

def main():
    domain = input("Enter a domain name (e.g., google.com): ").strip()
    if not domain:
        print("❌ No domain entered. Exiting.")
        return

    info = fetch_domain_info(domain)
    if info:
        save_to_csv(info)

if __name__ == "__main__":
    main()
