import yfinance as yf
import pandas as pd

def calculate_technical_indicators(df):
    # Calculate 20-day and 50-day Simple Moving Average (SMA)
    df['SMA20'] = df['Close'].rolling(window=20).mean()
    df['SMA50'] = df['Close'].rolling(window=50).mean()
    
    # Calculate Relative Strength Index (RSI) for 14 days
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI14'] = 100 - (100 / (1 + rs))

    return df

def fetch_and_save_stock_data(ticker, filename):
    # Fetch historical data for the given ticker
    print(f"Fetching data for {ticker}...")
    data = yf.download(ticker, period="1y")
    
    # Calculate technical indicators
    data_with_indicators = calculate_technical_indicators(data)
    
    # Save to a CSV file with ticker name in filepath
    output_path = f"{filename}/{ticker}_with_indicators.csv"
    data_with_indicators.to_csv(output_path)
    print(f"Data saved to {output_path}")

if __name__ == "__main__":
    # Load the list of stock tickers from the CSV file
    nifty50_file = "nifty50_historical_data.csv"
    tickers_df = pd.read_csv(nifty50_file)
    
    # Ensure there is a directory for output
    output_dir = "output_with_indicators"
    import os
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # To avoid duplicate processing, use a set to track processed tickers
    processed_tickers = set()
    
    # Fetch data, calculate indicators, and save to CSV for each stock
    for index, row in tickers_df.iterrows():
        stock_ticker = row['Ticker']
        if stock_ticker not in processed_tickers:
            fetch_and_save_stock_data(stock_ticker, output_dir)
            processed_tickers.add(stock_ticker)