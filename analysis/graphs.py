import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("db/stocks.db")

# Load data into pandas
df = pd.read_sql_query("SELECT * FROM stock_prices ORDER BY symbol, date", conn)

# Calculate daily change
df['daily_change'] = df.groupby('symbol')['close_price'].diff()

# Plot each stock
for stock in df['symbol'].unique():
    df_stock = df[df['symbol'] == stock]
    plt.figure(figsize=(10, 4))
    plt.plot(df_stock['date'], df_stock['close_price'], marker='o', label='Close Price')
    plt.plot(df_stock['date'], df_stock['daily_change'], marker='x', label='Daily Change')
    plt.title(f"{stock} Stock Prices & Daily Changes")
    plt.xticks(rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Price / Change")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"analysis/{stock}_graph.png")
    plt.show()

conn.close()
