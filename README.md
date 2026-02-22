# 📈 AI Stock Direction Prediction (AAPL)

An end-to-end **Machine Learning project** that predicts the **next-day stock movement (UP / DOWN)** for **Apple Inc. (AAPL)** using historical market data and technical indicators.

This project demonstrates a complete financial ML workflow — from **data collection** to **model evaluation and prediction generation**.

---

## 🔍 Project Objective

The goal of this project is to determine whether basic technical indicators can predict short-term stock direction **better than random guessing (~50%)**.

---

## 🧠 Machine Learning Pipeline

1. **Data Collection** from Yahoo Finance  
2. **Feature Engineering** (Technical Indicators)  
3. **Model Training** (Classification)  
4. **Model Evaluation**  
5. **Prediction Export**

---

## 🛠️ Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Scikit-learn**
- **yfinance**

---

## 📊 Features Used (Technical Indicators)

| Feature        | Description |
|---------------|-------------|
| **Daily_Return** | Percentage change in closing price |
| **MA5** | 5-day moving average (trend indicator) |
| **MA10** | 10-day moving average (trend indicator) |
| **Volatility** | 10-day rolling standard deviation (risk measure) |
| **RSI** | Relative Strength Index (momentum indicator) |
| **MACD** | Moving Average Convergence Divergence (trend + momentum) |

### 🎯 Target Variable

```
1 → Price goes UP next day  
0 → Price goes DOWN next day
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Download Stock Data
```bash
python src/stock_data.py
```

### 3️⃣ Generate Features
```bash
python src/feature_engineering.py
```

### 4️⃣ Train Models & Evaluate
```bash
python src/train_models.py
```

---

## 🤖 Models Used

- **Logistic Regression**
- **Random Forest Classifier**

---

## 📈 Results Summary

| Model | Accuracy |
|-------|----------|
| **Logistic Regression** | ~51–52% |
| **Random Forest** | ~50–51% |

The performance remained close to the random baseline, demonstrating the difficulty of predicting short-term stock movements using technical indicators alone.

---

## 📁 Output

The model generates:

```
outputs/model_predictions.csv
```

This file contains:

- Actual market movement
- Logistic Regression predictions
- Random Forest predictions

> ⚠️ Only ~20% of rows appear in this file because predictions are saved only for the **test dataset** (unseen data) after an 80/20 train-test split.

---

## 📚 Key Learnings

- Building a reproducible ML pipeline  
- Time-series feature engineering  
- Importance of evaluating on unseen data  
- Realistic expectations in financial prediction  
- Stock markets behave close to stochastic processes  

---

## 🚀 Future Improvements

- Add Bollinger Bands & ATR indicators  
- Rolling-window backtesting  
- Try **XGBoost / LightGBM**  
- Include sentiment or macroeconomic data  
- Simulate trading strategy with transaction costs  

---

## 👤 Author

**Krunal J. Patoliya**  
Waterloo, Ontario  

GitHub:  
https://github.com/krunalpatoliya7  

---

⭐ If you found this project helpful, consider giving it a star!
