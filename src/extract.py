import json 
from pathlib import Path

import requests

URL = "https://api.jolpi.ca/ergast/f1/2025/results.json"

HEADERS = {
    "User-Agent": "f1-data-pipeline/1.0"
}

response = requests.get(URL, headers=HEADERS, timeout=30)

response.raise_for_status()

data = response.json()

print("Data extracted successfully!")

print(data)
