import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import os
import re

file_name = "exchange_rates.csv"
url = "https://wise.com/de/currency-converter/usd-to-eur-rate"

headers = {"User-Agent": "Mozilla/5.0"}

# Get request
response = requests.get(url, headers=headers)
html = response.text

# Parse HTML
soup = BeautifulSoup(html, 'html.parser')
amount_span = soup.find('span', class_='d-inline-block', dir='ltr')

if amount_span:
    amount = amount_span.get_text(strip=True)

    # Regex to extract USD and EUR values
    pattern = r"\$(\d{1,3}(?:,\d{3})*)\s*USD\s*=\s*€([\d,\.]+)EUR"
    match = re.search(pattern, amount)

    if match:
        usd_raw = match.group(1)
        eur_raw = match.group(2)

        usd_value = usd_raw.replace(",", "") 
        eur_value = eur_raw.replace(",", ".")

        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [date_time, usd_value, eur_value]

        # Check if CSV exists
        file_exists = os.path.isfile(file_name)

        with open(file_name, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Date time", "USD", "EUR"])
            writer.writerow(row)
    else:
        print("❌ No match found in the extracted string.")
else:
    print("❌ Could not find the required span in the page.")
