"""Plotting functions for stock data."""
import matplotlib.pyplot as plt


def plot_stock_data(stock_data):
    """Plot stock data."""
    plt.figure(figsize=(15, 8))
    plt.title("Stock Prices History")
    plt.plot(stock_data["Close"])
    plt.xlabel("Date")
    plt.ylabel("Prices ($)")
