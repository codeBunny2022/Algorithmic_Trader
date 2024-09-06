import yfinance as yf
import pandas as pd

def fetch_nifty50_data():
    tickers = [
        'ADANIPORTS.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS', 'BAJFINANCE.NS',
        'BAJAJFINSV.NS', 'BPCL.NS', 'BHARTIARTL.NS', 'BRITANNIA.NS', 'CIPLA.NS',
        'COALINDIA.NS', 'DIVISLAB.NS', 'DRREDDY.NS', 'EICHERMOT.NS', 'GRASIM.NS',
        'HCLTECH.NS', 'HDFCBANK.NS', 'HDFC.NS', 'HEROMOTOCO.NS', 'HINDALCO.NS',
        'HINDUNILVR.NS', 'ICICIBANK.NS', 'INDUSINDBK.NS', 'INFY.NS', 'ITC.NS',
        'JSWSTEEL.NS', 'KOTAKBANK.NS', 'LT.NS', 'M&M.NS', 'MARUTI.NS',
        'NTPC.NS', 'ONGC.NS', 'POWERGRID.NS', 'RELIANCE.NS', 'SBIN.NS',
        'SUNPHARMA.NS', 'TCS.NS', 'TATACONSUM.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS',
        'TECHM.NS', 'TITAN.NS', 'UPL.NS', 'ULTRACEMCO.NS', 'VEDL.NS',
        'WIPRO.NS', 'ZEEL.NS'
    ]
    
    historical_data = {}
    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        data = yf.download(ticker, period="6mo")
        historical_data[ticker] = data

    combined_data = pd.concat(historical_data, names=['Ticker', 'Date'])
    
    return combined_data

if __name__ == "__main__":
    df = fetch_nifty50_data()
    print(df)
    df.to_csv('nifty50_historical_data.csv')