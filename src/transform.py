import json
from pathlib import Path

input_path = Path("data") / "race_results_2025.json"

with open(input_path, "r", encoding="utf-8") as file:
    races = json.load(file)

rows = []


for race in races:
    for result in race["Results"]:
        row = {
            "season": race["season"],
            "round": race["round"],
            "race_name": race["raceName"],
            "date": race["date"],
            "driver_id": result["Driver"]["driverId"],
            "driver_name": (
                result["Driver"]["givenName"]
                + " "
                + result["Driver"]["familyName"]
            ),
            "constructor_id": result["Constructor"]["constructorId"],
            "constructor_name": result["Constructor"]["name"],
            "grid": result["grid"],
            "position": result["position"],
            "points": result["points"],
            "laps": result["laps"],
            "status": result["status"]
        }

        rows.append(row)

print(f"Rows created: {len(rows)}")
print(rows[0])