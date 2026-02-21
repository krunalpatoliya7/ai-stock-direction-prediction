import yfinance as yf
import pandas as pd
import os

# Choose stock ticker
ticker = "AAPL"

# Download historical stock data
df = yf.download(ticker, start="2018-01-01", end="2023-12-31")

# Save CSV in the same folder
save_path = os.path.join(os.getcwd(), f"{ticker}_stock_data.csv")
df.to_csv(save_path)

print(f"Data saved at: {save_path}")
