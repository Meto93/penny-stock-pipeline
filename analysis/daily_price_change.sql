SELECT
    symbol,
    date,
    close_price,
    close_price
      - LAG(close_price)
        OVER (PARTITION BY symbol ORDER BY date) AS daily_change
FROM stock_prices
ORDER BY symbol, date;
