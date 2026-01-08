import sqlite3
import csv
import os

DB_PATH = "db/stocks.db"
CSV_PATH = "data/raw/stock_prices.csv"

os.makedirs("db", exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS stock_prices (
    symbol TEXT,
    date TEXT,
    close_price REAL,
    volume INTEGER
)
""")

with open(CSV_PATH, "r") as f:
    reader = csv.DictReader(f)
    rows = [
        (r["symbol"], r["date"], r["close_price"], r["volume"])
        for r in reader
    ]

cursor.executemany(
    "INSERT INTO stock_prices VALUES (?, ?, ?, ?)",
    rows
)

conn.commit()
conn.close()

print("Data loaded into SQLite database")
