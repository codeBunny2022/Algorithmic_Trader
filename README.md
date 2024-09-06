# Trade Signal Generation and Analysis Project

## Introduction
This project fetches historical stock data, calculates technical indicators, generates trade signals, and analyzes the performance of the trade signals.

## Project Flow
1. **Fetch Historical Data**: Using yFinance to fetch historical stock data.
2. **Calculate Technical Indicators**: Calculate 20-day and 50-day Simple Moving Average (SMA) and Relative Strength Index (RSI).
3. **Generate Trade Signals**:
    - Buy when 20-day SMA crosses 50-day SMA from below.
    - Sell when 20-day SMA crosses 50-day SMA from above.
    - Buy when RSI < 30.
    - Sell when RSI > 70.
4. **Analyze Trade Signals**:
    - Randomly select 5 stocks from the Nifty 50 and analyze their performance based on the trade signals for the last 6 months.
  
## Analysis Report
### Summary
- **Total Profit**: 1829.699462890625
- **Total Loss**: 0.0
- **Net Result**: 1829.699462890625
- **Number of Profitable Stocks**: 4
- **Number of Loss Stocks**: 1

### Detailed Results
| Stock | Net Gain/Loss | Status |
|-------|----------------|--------|
| ULTRACEMCO.NS | 680.6494140625 | Profit |
| GRASIM.NS | 128.050048828125 | Profit |
| HEROMOTOCO.NS | 904.60009765625 | Profit |
| TATASTEEL.NS | 0.0 | Loss |
| SUNPHARMA.NS | 116.39990234375 | Profit |