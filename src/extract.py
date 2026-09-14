import json 
from pathlib import Path

import requests

#URL = "https://api.jolpi.ca/ergast/f1/2025/results.json"

HEADERS = {
    "User-Agent": "f1-data-pipeline/1.0"
}

all_races = []

offset = 0
limit = 30

while True:
    url = (
        f"https://api.jolpi.ca/ergast/f1/2025/results.json"
        f"?limit={limit}&offset={offset}"
    )
    
    response = requests.get(url, headers=HEADERS, timeout=30)

    response.raise_for_status()

    data = response.json()

    races = data["MRData"]["RaceTable"]["Races"]

    all_races.extend(races)

    total = int(data["MRData"]["total"])

    print(f"Fetched offset {offset}")

    offset += limit

    if offset >= total:
        break

#print("Data extracted successfully!")



#Merge races that were split across API pages
merged_races = {}

for race in all_races:
    round_number = race["round"]

    if round_number not in merged_races:
        merged_races[round_number] = race
    else:
        merged_races[round_number]["Results"].extend(race["Results"])


#Convert dictionary back to a list
final_races = list(merged_races.values())

#Check everything wsas collected 
print(f"Total races fetched: {len(final_races)}")

total_results = sum(len(race["Results"]) for race in final_races)

print(f"Total driver results fetched: {total_results}")




output_path = Path("data") / "race_results_2025.json"

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(final_races, file, indent=4)

print (f"Data saved to {output_path}")

#print(data["MRData"]["RaceTable"].keys())

#races = data["MRData"]["RaceTable"]["Races"]

#print(type(races))
#print(len(races))

#first_race = races[0]
#print(first_race.keys())




#results = first_race["Results"]

#print(type(results))
#print(len(results))

#first_result = results[0]
#print(first_result.keys())



#print(first_result["Driver"])
#print(first_result["Constructor"])



#print("Limit:", data["MRData"]["limit"])
#print("Offset:", data["MRData"]["offset"])
#print("Total:", data["MRData"]["total"])


