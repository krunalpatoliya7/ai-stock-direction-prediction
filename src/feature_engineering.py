import pandas as pd

# ==========================================
# feature_engineering.py (FINAL - Day 4)
# Input : AAPL_stock_data.csv
# Output: AAPL_stock_features.csv
# Adds  : Daily_Return, MA5, MA10, Volatility, RSI, MACD, Target
# ==========================================

INPUT_FILE = "AAPL_stock_data.csv"
OUTPUT_FILE = "AAPL_stock_features.csv"

# 1) Load CSV
# Your CSV contains an extra second row like: "Ticker AAPL AAPL ..."
df = pd.read_csv(
    INPUT_FILE,
    skiprows=[1],     # skip ticker row
    index_col=0       # first column is Date
)

# 2) Parse Date index safely
df.index = pd.to_datetime(df.index, errors="coerce")
df = df[~df.index.isna()]  # remove rows where date failed parsing

# 3) Convert numeric columns safely (your CSV uses these columns)
numeric_cols = ["Price", "Close", "High", "Low", "Open", "Volume"]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows where Close is missing (needed for indicators)
df.dropna(subset=["Close"], inplace=True)

# 4) Feature Engineering

# Daily Return
df["Daily_Return"] = df["Close"].pct_change()

# Moving Averages
df["MA5"] = df["Close"].rolling(window=5).mean()
df["MA10"] = df["Close"].rolling(window=10).mean()

# Volatility (10-day rolling std of daily returns)
df["Volatility"] = df["Daily_Return"].rolling(window=10).std()

# RSI (14-day)
window = 14
delta = df["Close"].diff()

gain = delta.clip(lower=0)
loss = -delta.clip(upper=0)

avg_gain = gain.rolling(window=window).mean()
avg_loss = loss.rolling(window=window).mean()

rs = avg_gain / avg_loss
df["RSI"] = 100 - (100 / (1 + rs))

# MACD (12 EMA - 26 EMA)
ema12 = df["Close"].ewm(span=12, adjust=False).mean()
ema26 = df["Close"].ewm(span=26, adjust=False).mean()
df["MACD"] = ema12 - ema26

# 5) Target Variable (Up/Down)
# 1 if next day's Close > today's Close else 0
df["Target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)

# 6) Drop rows with missing values created by rolling indicators
df.dropna(inplace=True)

# 7) Save dataset
df.to_csv(OUTPUT_FILE)

# 8) Print verification
print("\n✅ Feature Engineering Completed!")
print("Saved file:", OUTPUT_FILE)

print("\nColumns in final dataset:")
print(df.columns)

print("\nFirst 5 rows preview:")
print(df.head())