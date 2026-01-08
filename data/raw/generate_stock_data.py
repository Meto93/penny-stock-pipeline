import csv
import random
from datetime import datetime, timedelta

STOCKS = ["ABC", "XYZ", "PENY"]
DAYS = 30

start_date = datetime.now() - timedelta(days=DAYS)

rows = []

for stock in STOCKS:
    price = round(random.uniform(0.5, 5.0), 2)
    for day in range(DAYS):
        date = start_date + timedelta(days=day)
        change = round(random.uniform(-0.3, 0.3), 2)
        price = max(0.1, round(price + change, 2))

        rows.append({
            "symbol": stock,
            "date": date.date().isoformat(),
            "close_price": price,
            "volume": random.randint(10_000, 200_000)
        })

with open("data/raw/stock_prices.csv", "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["symbol", "date", "close_price", "volume"]
    )
    writer.writeheader()
    writer.writerows(rows)

print("Generated stock_prices.csv")
