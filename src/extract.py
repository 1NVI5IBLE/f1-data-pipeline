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



output_path = Path("data") / "race_results_2025.json"

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print (f"Data saved to {output_path}")

print(data["MRData"]["RaceTable"].keys())



races = data["MRData"]["RaceTable"]["Races"]

print(type(races))
print(len(races))

first_race = races[0]
print(first_race.keys())




results = first_race["Results"]

print(type(results))
print(len(results))

first_result = results[0]
print(first_result.keys())



print(first_result["Driver"])
print(first_result["Constructor"])


