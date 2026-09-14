import os

import psycopg2

connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="f1_data",
    user="postgres",
    password=os.getenv("POSTGRES_PASSWORD")
)

print("Connected to PostgreSQL database successfully!")

connection.close()