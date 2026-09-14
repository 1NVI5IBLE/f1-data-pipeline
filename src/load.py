import json
import os
from pathlib import Path

import psycopg2

input_path = Path("data") / "race_results_2025.json"

with open(input_path, "r", encoding="utf-8") as file:
    races = json.load(file)

rows = []

for race in races:
    for result in race["Results"]:
        row = (
            int(race["season"]),
            int(race["round"]),
            race["raceName"],
            race["date"],
            result["Driver"]["driverId"],
            result["Driver"]["givenName"] + " " + result["Driver"]["familyName"],
            result["Constructor"]["constructorId"],
            result["Constructor"]["name"],
            int(result["grid"]),
            int(result["position"]),
            float(result["points"]),
            int(result["laps"]),
            result["status"]
        )

        rows.append(row)

connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="f1_data",
    user="postgres",
    password=os.getenv("POSTGRES_PASSWORD")
)

cursor = connection.cursor()

insert_query = """
INSERT INTO race_results (
    season,
    round,
    race_name,
    race_date,
    driver_id,
    driver_name,
    constructor_id,
    constructor_name,
    grid_position,
    finish_position,
    points,
    laps,
    status
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

cursor.executemany(insert_query, rows)

connection.commit()

print(f"Inserted {len(rows)} rows into PostgreSQL")

print("Connected to PostgreSQL database successfully!")

cursor.close()
connection.close()