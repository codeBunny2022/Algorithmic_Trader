import yfinance as yf
import pandas as pd
import os

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

def generate_trade_signals(df):
    # Initialize columns
    df['Signal'] = ''
    
    # Generate SMA signals
    df.loc[(df['SMA20'] > df['SMA50']) & (df['SMA20'].shift(1) <= df['SMA50'].shift(1)), 'Signal'] = 'Buy'
    df.loc[(df['SMA20'] < df['SMA50']) & (df['SMA20'].shift(1) >= df['SMA50'].shift(1)), 'Signal'] = 'Sell'
    
    # Generate RSI signals
    df.loc[df['RSI14'] < 30, 'Signal'] = 'Buy'
    df.loc[df['RSI14'] > 70, 'Signal'] = 'Sell'

    return df

if __name__ == "__main__":
    # Ensure there is a directory for output_with_indicators data
    output_dir = "output_with_indicators"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Load the list of stock tickers from the CSV file
    nifty50_file = "nifty50_historical_data.csv"
    tickers_df = pd.read_csv(nifty50_file)
    
    # Fetch data, calculate indicators, and save to CSV for each stock
    processed_tickers = set()
    for index, row in tickers_df.iterrows():
        stock_ticker = row['Ticker']
        if stock_ticker not in processed_tickers:
            fetch_and_save_stock_data(stock_ticker, output_dir)
            processed_tickers.add(stock_ticker)
    
    # Ensure there is a directory for signal output
    signals_output_dir = "output_with_signals"
    if not os.path.exists(signals_output_dir):
        os.makedirs(signals_output_dir)
    
    # Generate trade signals for each stock in output_with_indicators
    for filename in os.listdir(output_dir):
        if filename.endswith("_with_indicators.csv"):
            stock_ticker = filename.split('_with_indicators.csv')[0]
            df = pd.read_csv(os.path.join(output_dir, filename))
            
            # Generate trade signals
            df_with_signals = generate_trade_signals(df)
            
            # Save the signals to a new CSV file in the signals_output_dir
            signal_output_path = os.path.join(signals_output_dir, f"{stock_ticker}_with_signals.csv")
            df_with_signals.to_csv(signal_output_path)
            print(f"Trade signals saved to {signal_output_path}")