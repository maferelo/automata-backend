"""Get stock data."""
import yfinance as yf


def get_stock_data():
    """Get stock data from Yahoo Finance."""
    return yf.download("AAPL", start="2016-01-01", end="2021-10-01")
