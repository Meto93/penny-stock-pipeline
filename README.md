# Penny Stock Data Pipeline

## Overview
This project simulates an automated data pipeline for penny stock prices.  
It demonstrates basic **automation, data ingestion, SQL analysis, and visualization** skills.

## Features
- Generate simulated stock price data (CSV)  
- Store raw data in a **SQLite database**  
- Calculate daily price changes using **SQL**  
- Visualize stock prices and daily changes using **Python + Matplotlib**  

## Tech Stack
- Python 3.x  
- SQLite  
- pandas  
- matplotlib  

## Folder Structure
penny-stock-pipeline/
data/
raw/ # Generated CSV data
db/ # SQLite database
ingestion/ # Scripts to load data into DB
analysis/ # SQL queries and graphs
logs/ # Optional logs
README.md


## How to Run
1. Generate stock data:
python data\raw\generate_stock_data.py

2.Load CSV into database
python ingestion\load_to_db.py

3.Run analysis and generate graphs:
python analysis\graphs.py